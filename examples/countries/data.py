"""
Named tuple example
===================

Generating a population density report from data organized
as named tuples, with a ``density`` helper function::

    >>> report()
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

"""

import collections

pop10 = [
    ("China", 1_394_897_526, 9_640_821),
    ("India", 1_338_906_197, 3_287_240),
    ("United States", 328_088_060, 9_833_517),
    ("Indonesia", 265_015_300, 1_904_569),
    ("Brazil", 209_780_729, 8_515_767),
    ("Pakistan", 202_499_217, 803_940),
    ("Nigeria", 195_875_237, 923_768),
    ("Bangladesh", 165_446_400, 143_998),
    ("Russia", 146_877_088, 17_125_242),
    ("Japan", 126_440_000, 377_944),
]

CountryRecord = collections.namedtuple("Country", "name population area")


def report():

    data = [CountryRecord(*t) for t in pop10]

    def density(country):
        return country.population / country.area

    data.sort(key=density, reverse=True)

    for country in data:
        print(f"{density(country):6.1f}  {country.name}")


if __name__ == "__main__":
    report()
