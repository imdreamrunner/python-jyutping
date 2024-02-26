# -*- coding: utf-8 -*-
"""
Convert Chinese characters to Jyutping.
"""
from __future__ import absolute_import
from urllib import parse
import requests
from opencc import OpenCC
from . import dictionary, online


def get_jyutping(characters, multiple=False, online=False):
    """
    Convert Chinese characters to Jyutping.
    @return an array of Jyutping for each character.
    """
    result = []
    for ch in characters:
        if online:
            jyutpings = search_online(ch, multiple)
        else:
            jyutpings = search(ch, multiple)
        result.append(jyutpings)
    return result


def search(character, multiple=False):
    if not dictionary.CHS_DICT or not dictionary.CHT_DICT:
        dictionary.load_dictionary()
    jyupings = dictionary.CHS_DICT.get(character, set()) | dictionary.CHT_DICT.get(
        character, set()
    )
    if multiple:
        return jyupings
    else:
        return jyupings.pop() if jyupings else None


def search_online(character, multiple=False):
    assert (
        len(character) == 1 and '\u4e00' <= character <= '\u9fff'
    ), 'Input must be a single Chinese character.'
    cc = OpenCC('s2t')
    character = cc.convert(character)
    encoded_character = parse.quote(character.encode('big5'))
    response = requests.get(
        f'https://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/search.php?q={encoded_character}'
    )
    return online.parse_response(response, multiple)


def _test(word):
    print(word, get_jyutping(word))
    print(word, get_jyutping(word, multiple=True))
    print(word, get_jyutping(word, online=True))
    print(word, get_jyutping(word, multiple=True, online=True))


if __name__ == '__main__':
    _test('广东话')
