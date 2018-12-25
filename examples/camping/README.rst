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

Running tests
-------------

To run these doctests on **bash** use this command line::

    $ python3 -m doctest README.rst
