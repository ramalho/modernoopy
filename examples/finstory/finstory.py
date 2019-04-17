"""
``FinancialHistory`` keeps track of a person's expenses,
income, and balance.

Create ``FinancialHistory`` with $ 100.

    >>> h = FinancialHistory('100')
    >>> h
    <FinancialHistory(100.00): 0 transactions>

Spend some money::

    >>> h.spend('39.95', 'meal')
    >>> h
    <FinancialHistory(60.05): 1 transaction>
    >>> h.balance
    Decimal('60.05')

Decimals can be formatted like floats::

    >>> print(f'${h.balance:0.2f}')
    $60.05

Get more money::

    >>> h.receive(1000.01, "Molly's game")
    >>> h.receive(10.01, 'found on street')
    >>> h
    <FinancialHistory(1070.07): 3 transactions>

Spend more money::

    >>> h.spend(55.35, 'meal')
    >>> h.spend(26.65, 'meal')
    >>> h.spend(300, 'concert')
    >>> h
    <FinancialHistory(688.07): 6 transactions>

Check amount spent on meals::

    >>> h.spent_for('meal')
    Decimal('121.95')

Check amount spent on travel (zero):

    >>> h.spent_for('travel')
    Decimal('0')

Statement:

    >>> for line in h.statement():  # doctest: +NORMALIZE_WHITESPACE
    ...   print(line)
    # initial balance    +100.00
    meal                  -39.95
    Molly's game        +1000.01
    found on street       +10.01
    meal                  -55.35
    meal                  -26.65
    concert              -300.00
    # current balance    +688.07


"""

import collections
import decimal


decimal.setcontext(decimal.BasicContext)


def clean_decimal(value):
    """Builds a Decimal using the cleaner float `repr`"""
    if isinstance(value, float):
        value = repr(value)
    return decimal.Decimal(value)


Transaction = collections.namedtuple("Transaction", "amount description")


class FinancialHistory:

    def __init__(self, amount=0):
        self._initial_balance = clean_decimal(amount)
        self._history = []

    def __repr__(self):
        bal = self.balance
        len_hist = len(self._history)
        plural = 's' if len_hist != 1 else ''
        return f'<FinancialHistory({bal:0.2f}): {len_hist} transaction{plural}>'

    def receive(self, amount, source):
        amount = clean_decimal(amount)
        self._history.append(Transaction(amount, source))

    def spend(self, amount, reason):
        amount = -clean_decimal(amount)
        self._history.append(Transaction(amount, reason))

    @property
    def balance(self):
        return self._initial_balance + sum(t.amount for t in self._history)

    def spent_for(self, reason):
        select = (t.amount for t in self._history if t.description == reason)
        return -sum(select, clean_decimal(0))

    def statement(self):
        line_fmt = '{reason:12}\t{value:+12.2f}'
        balance = self._initial_balance
        msg = '# initial balance'
        yield line_fmt.format(reason=msg, value=balance)
        for t in self._history:
            yield line_fmt.format(reason=t.description,
                                  value=t.amount)
            balance += t.amount
        msg = '# current balance'
        yield line_fmt.format(reason=msg, value=balance)
