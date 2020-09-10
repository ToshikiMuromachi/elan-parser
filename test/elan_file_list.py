#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import glob  # Import glob to easily loop over files
import os
import pympi  # Import pympi to work with elan files
import string  # Import string to get the punctuation data


if __name__ == '__main__':
    corpus_root = '/home/share/underpin/RecordVoice/Nohin_1207/'
    output_root = '/home/tmuromachi/data/output/ELAN/underpin/'
    ort_tier_names = ['医師', '患者']  # 話者
    # corpus_root = '/home/toshiki/data/Chiba3Party/ELAN/'
    # corpus_root = '/home/share/underpin/Transcript/'
    # output_root = '/home/tmuromachi/data/ELAN/'
    # ort_tier_names = ['A.luu', 'B.luu', 'C.luu']  # 話者

    for pathname, dirnames, filenames in os.walk(corpus_root):
        for filename in filenames:
            if filename.endswith('.eaf') and not filename.startswith('.'):
                input_path = pathname + filename
                print(input_path)
