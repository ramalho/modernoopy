Camping Budget Example
======================

Class ``camping.Budget`` represents the budget for a camping trip
in which the people who pitched in more than average need to be
reimbursed by the others.

    >>> from camping import Budget
    >>> b = Budget("Debbie Ann Bob Charlie")
    >>> b.total()
    0.0
    >>> b.people()
    ['Ann', 'Bob', 'Charlie', 'Debbie']
    >>> b.contribute("Bob", 50.00)
    >>> b.contribute("Debbie", 40.00)
    >>> b.contribute("Ann", 10.00)
    >>> b.total()
    100.0

The ``report`` method lists who should receive or pay, and the
respective amounts.

    >>> b.report()
      Total: $100.00; per person: $ 25.00
    ----------------------------------------
           Ann paid $ 10.00, owes $ 15.00
           Bob paid $ 50.00, gets $ 25.00
       Charlie paid $  0.00, owes $ 25.00
        Debbie paid $ 40.00, gets $ 15.00

The data used by ``repor`` is computed by the `balances` generator:

    >>> b.balances()  # doctest:+ELLIPSIS
    <generator object Budget.balances at 0x...>
    >>> list(b.balances())
    [('Ann', 10.0, -15.0), ('Bob', 50.0, 25.0), ('Charlie', 0.0, -25.0), ('Debbie', 40.0, 15.0)]

Running tests
-------------

To run these doctests on **bash** use this command line::

    $ python3 -m doctest README.rst
