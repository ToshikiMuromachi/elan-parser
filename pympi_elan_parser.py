#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import glob  # Import glob to easily loop over files
import os
import pympi  # Import pympi to work with elan files
import string  # Import string to get the punctuation data


def elan_read(file_path):
    """
    ELANファイルを解析後、二次元リストとして返す
    :param file_path: ファイルパス
    :return: ELAN解析結果
    """
    # elanファイル初期化
    eafob = pympi.Elan.Eaf(file_path)
    # 1ファイルの全発話
    elan_data = []

    # 話者ごとにループ
    for ort_tier in ort_tier_names:
        if ort_tier not in eafob.get_tier_names():
            print('WARNING!!!')
            print('One of the ortography tiers is not present in the elan file')
            print('namely: {}. skipping this one...'.format(ort_tier))
        else:
            for annotation in eafob.get_annotation_data_for_tier(ort_tier):
                start_time = annotation[0]
                end_time = annotation[1]
                utterance = annotation[2]

                elan_data.append([start_time, end_time, ort_tier, utterance])
    return elan_data


def elan_write(file_path, data):
    """
    ELANファイル解析結果をoutputディレクトリにcsvとして書き込み
    :param file_path:解析するファイルパス
    :param data:ELANファイル解析結果
    :return:
    """
    output_path = output_root + os.path.splitext(os.path.basename(file_path))[0] + '.csv'
    with open(output_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)


if __name__ == '__main__':
    # corpus_root = '/home/toshiki/data/Chiba3Party/ELAN/'
    # output_root = '/home/toshiki/data/output/ELAN/'
    # ort_tier_names = ['A.luu', 'B.luu', 'C.luu']  # 話者
    corpus_root = '/home/share/underpin/Transcript/'
    output_root = '/home/tmuromachi/data/ELAN/'
    ort_tier_names = ['医師', '患者']  # 話者

    for pathname, dirnames, filenames in os.walk(corpus_root):
        for filename in filenames:
            if filename.endswith('.eaf'):
                input_path = pathname + "/" + filename
                file_data = elan_read(input_path)
                elan_write(input_path, file_data)

                print("--*--*--*--")
                print(input_path)
                print(file_data)
