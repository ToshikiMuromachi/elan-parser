#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob  # Import glob to easily loop over files
import pympi  # Import pympi to work with elan files
import string  # Import string to get the punctuation data


def elan_read(file_path):
    """
    ELANファイル読み込み後tab区切りで返す
    :param file_path:
    :return:
    """
    # elanファイル初期化
    eafob = pympi.Elan.Eaf(file_path)
    # 1ファイルの全発話
    elan_data = [[]]

    # 話者ごとにループ
    for ort_tier in ort_tier_names:
        # 層がelanファイルに存在しない場合、エラーを発生させて続行
        if ort_tier not in eafob.get_tier_names():
            print('WARNING!!!')
            print('One of the ortography tiers is not present in the elan file')
            print('namely: {}. skipping this one...'.format(ort_tier))
        # 層が存在する場合、アノテーションデータをループ
        else:
            for annotation in eafob.get_annotation_data_for_tier(ort_tier):
                # 発話のみ取得
                start_time = annotation[0]
                end_time = annotation[1]
                utterance = annotation[2]

                elan_data.append([start_time, end_time, utterance])
                # print(start_time, end_time, ort_tier, utterance)
    return elan_data


if __name__ == '__main__':
    corpus_root = '/home/toshiki/data/Chiba3Party/ELAN'
    output_file = '/home/toshiki/data/output/ELAN/'
    ort_tier_names = ['A.luu', 'B.luu', 'C.luu']  # 話者

    for f in glob.glob('{}/*.eaf'.format(corpus_root)):
        print("--*--*--*--")
        print(f)
        print(elan_read(f))
