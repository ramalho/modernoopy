Data class example: Country
===========================

``Country`` is a data class. Data classes are created and managed
with clsses and functions from the ``dataclasses`` standard module::

    >>> from countries import Country
    >>> from dataclasses import fields
    >>> for f in fields(Country):
    ...     print(f.name, f.type)
    name <class 'str'>
    population <class 'float'>
    area <class 'float'>

``Country`` inherits a ``__repr__``::

    >>> cn = Country('China', 1_394_897_526, 9_640_821)
    >>> cn
    Country(name='China', population=1394897526, area=9640821)

``Country`` implements a ``density`` method::

    >>> Country.density.__doc__
    'population density in persons/km²'
    >>> cn.density()
    144.68659111086077


Population density ranking
--------------------------

List of 10 most populous countries, sorted by population density::

    >>> from data import pop10
    >>> data = [Country(*t) for t in pop10]
    >>> data.sort(key=Country.density, reverse=True)
    >>> for country in data:
    ...     print(f"{country.density():6.1f}  {country.name}")
    1148.9  Bangladesh
     407.3  India
     334.5  Japan
     251.9  Pakistan
     212.0  Nigeria
     144.7  China
     139.1  Indonesia
      33.4  United States
      24.6  Brazil
       8.6  Russia


