import csv
import glob
import os
import pandas as pd

input_root = '/home/toshiki/data/output/aizuchi/chiba3/aizuchi-predict/unsort/'
output_root = '/home/toshiki/data/output/aizuchi/chiba3/aizuchi-predict/sort/'

# input_root = '/mnt/c/data/output/unsort/'
# output_root = '/mnt/c/data/output/sort/'
# input_root = '/home/tmuromachi/data/ELAN/underpin/unsort/'
# output_root = '/home/tmuromachi/data/ELAN/underpin/sort/'
# input_root = '/home/toshiki/data/output/ELAN/'
# output_root = '/home/toshiki/data/output/ELAN_analysis/'

for f in glob.glob('{}/*.csv'.format(input_root)):
    print(f)
    df = pd.read_csv(f, header=None)
    df_s = df.sort_values(0)
    df_s = df_s.reset_index(drop=True)
    print(df_s)

    output_path = output_root + os.path.basename(f)
    print("->output to : " + output_path)
    df_s.to_csv(output_path, header=False, encoding="utf-8")
