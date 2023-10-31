# config.py - file with reusable static constants and other pieces of config data
from pathlib import Path

# runtime config

def isFastMode():
    # mode = "fast" # fast mode reduces the cohort size, but executes 10 to 20x faster, good for debugging, but final report should use full mode
    mode = "fast"
    return mode == "fast"


root = Path('..')

# data paths
data_dir = root / 'data'
ddinter_data_dir = data_dir / 'ddinter'

drugbank_data_file = data_dir / 'drugbank' / 'drugbank_vocab.csv'

icd_data_file = data_dir / 'icd' / 'amiajnl-2013-002116-s1-ranked_icd_codes.csv'

## output paths
out_dir = root / 'out'
cohort_fast_out_file = out_dir / 'cohort-fast.out'
cohort_full_out_file = out_dir / 'cohort-full.out'

cohort_no_icd_out_file = out_dir / 'cohort-no-icd-file.out'

emar_interactions_out_file = out_dir / 'emar-drug-interactions.out'
icu_interactions_out_file = out_dir / 'icu-drug-interactions.out'
total_interactions_out_file = out_dir / 'total-drug-interactions.out'

bp_results_out_file = out_dir / 'bp_raw_data.out'

## DB tables
icu_d_items = '`physionet-data.mimiciv_icu.d_items`'
hosp = "physionet-data.mimiciv_hosp"

# %%
