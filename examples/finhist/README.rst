Financial History Example
=========================

``FinancialHistory`` instances keep track of a person's expenses and income.

.. note::  This example is adapted from *Smalltalk-80: the language*, by Adele Goldberg and Dave Robson (Addison-Wesley, 1989). 

The interface of ``FinancialHistory`` consists of:

``__init__(amount)``
    Begin a financial history with an amount given (default: 0).

``__repr__``
    Return string representation of the instance, for debugging.

``receive(amount, source)``
    Receive an amount from the named source.

``spend(amount, reason)``
    Spend an amount for the named reason.

``balance()``
    Return total amount currenly on hand.

``received_from(source)``
    Return total amount received from the given source.

``spent_for(reason)``
    Return total amount spent for the given reason.
