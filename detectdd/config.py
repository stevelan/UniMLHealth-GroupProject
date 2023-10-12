# config.py - file with reusable static constants and other pieces of config data
from pathlib import Path

root = Path('..')

# data paths
data_dir = root / 'data'
ddinter_data_dir = data_dir / 'ddinter'

drugbank_data_file = data_dir / 'drugbank' / 'drugbank_vocab.csv'

## output paths
out_dir = root / 'out'
cohort_out_file = out_dir / 'cohort.out'

## DB tables
icu_d_items = '`physionet-data.mimiciv_icu.d_items`'

#%%
