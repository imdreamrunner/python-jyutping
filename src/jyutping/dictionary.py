"""
Dictionary
"""
from __future__ import absolute_import
from collections import defaultdict
import os
import io
from jyutping import logger

CHT_DICT = defaultdict(set)
CHS_DICT = defaultdict(set)


def load_dictionary():
    source_path = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(source_path, 'data')
    dictionary_file = os.listdir(data_path)[0]
    logger.log('Load dictionary %s.' % dictionary_file)
    dictionary_file_full_path = os.path.join(data_path, dictionary_file)
    with io.open(dictionary_file_full_path, mode='r', encoding='utf-8') as f:
        index = 0
        for line in f:
            index += 1
            if index < 10:
                continue
            line = line.strip().split('\t')
            cht, chs, jyp = line
            if '/' in jyp:
                jyps = set(jyp.split('/'))
            else:
                jyps = set([jyp])
            CHT_DICT[cht].update(jyps)
            CHS_DICT[chs].update(jyps)


if __name__ == '__main__':
    load_dictionary()
