#!/usr/bin/env python3
"""
Find Unicode characters by name.

Example::

    >>> find(['cat', 'eyes'])  # doctest: +NORMALIZE_WHITESPACE
    U+1F638	😸	GRINNING CAT FACE WITH SMILING EYES
    U+1F63B	😻	SMILING CAT FACE WITH HEART-SHAPED EYES
    U+1F63D	😽	KISSING CAT FACE WITH CLOSED EYES

"""


import unicodedata
import sys

import index


def build_index():
    idx = index.Index()
    for i in range(32, sys.maxunicode + 1):
        char = chr(i)
        for word in unicodedata.name(char, "").split():
            idx.add(word, char)
    return idx


def find(words):
    idx = build_index()
    results = idx.get(*[w.upper() for w in words])
    if results:
        for char in sorted(results):
            name = unicodedata.name(char)
            print(f"U+{ord(char):04X}\t{char}\t{name}")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        find(sys.argv[1:])
    else:
        print("Please provide word(s) to search.")
