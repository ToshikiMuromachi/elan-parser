#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import glob  # Import glob to easily loop over files
import os
import pympi  # Import pympi to work with elan files
import string  # Import string to get the punctuation data


if __name__ == '__main__':
    corpus_root = '/xxx/'
    output_root = '/xxx/'
    ort_tier_names = ['医師', '患者']  # 話者
    # ort_tier_names = ['A.luu', 'B.luu', 'C.luu']  # 話者

    for pathname, dirnames, filenames in os.walk(corpus_root):
        for filename in filenames:
            if filename.endswith('.eaf') and not filename.startswith('.'):
                input_path = pathname + "/" + filename
                print(input_path)
                print(filename)
