# -*- coding: utf-8 -*-
"""
Convert Chinese characters to Jyutping.
"""
from __future__ import absolute_import
from jyutping import dictionary

def get_jyutping(characters, multiple=False):
    """
    Convert Chinese characters to Jyutping.
    @return an array of Jyutping for each character.
    """
    result = []
    for ch in characters:
        result.append(search(ch, multiple))
    return result


def search(character, multiple=False):
    if not dictionary.CHS_DICT or not dictionary.CHT_DICT:
        dictionary.load_dictionary()
    jyupings = dictionary.CHS_DICT.get(character, set()) | dictionary.CHT_DICT.get(character, set())
    if multiple:
        return jyupings
    else:
        return jyupings.pop() if jyupings else None


def _test(word):
    print(word, get_jyutping(word))
    print(word, get_jyutping(word, True))

if __name__ == '__main__':
    _test('广东话')
