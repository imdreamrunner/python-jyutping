# -*- coding: utf-8 -*-
"""
Convert Chinese characters to Jyutping.
"""
from __future__ import absolute_import
from jyutping import dictionary

def get_jyutping(characters):
    """
    Convert Chinese characters to Jyutping.
    @return an array of Jyutping for each character.
    """
    result = []
    for ch in characters:
        result.append(search_single(ch))
    return result


def search_single(character):
    if len(dictionary.CHS_DICT) == 0 or len(dictionary.CHT_DICT) == 0:
        dictionary.load_dictionary()
    jyp = dictionary.CHS_DICT.get(character) or dictionary.CHT_DICT.get(character)
    if jyp and '/' in jyp:
        jyp = jyp.split('/')
    return jyp


def _test(word):
    print(word, get_jyutping(word))

if __name__ == '__main__':
    _test('广东话')
