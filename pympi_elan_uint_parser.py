import csv
import os

import pympi



if __name__ == '__main__':
    # corpus_root = '/home/share/underpin/Transcript/'
    # output_root = '/home/tmuromachi/data/ELAN/'
    ort_tier_names = ['医師', '患者']  # 話者

    # corpus_root = '/home/toshiki/data/Chiba3Party/ELAN/'
    # output_root = '/home/toshiki/data/output/ELAN/'
    # ort_tier_names = ['A.luu', 'B.luu', 'C.luu']  # 話者

    # input_path = '/home/share/underpin/Transcript-20200226/UKM014-1/Uncheck/UKM014-1_3.eaf'
    input_path = '/home/share/underpin/RecordVoice/Nohin_1207/UKM029-2_3.eaf'
    output_root = '/home/tmuromachi/data/ELAN/'

    # elanファイル初期化
    eafob = pympi.Elan.Eaf(input_path)
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

    output_path = output_root + os.path.splitext(os.path.basename(input_path))[0] + '.csv'
    with open(output_path, 'w', encoding='utf_8') as file:
        writer = csv.writer(file)
        writer.writerows(elan_data)

    print("--*--*--*--")
    print(input_path)
    print(elan_data)
