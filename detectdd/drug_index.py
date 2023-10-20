# drug_index.py - loads the synonym drug index from the drugbank data.
# See DrugIndexTestCase for tests
from detectdd.config import *
import pandas as pd
class Synonym:
    def __init__(self, id, common_name, synonym):
        self.id = id
        self.common_name = common_name
        self.synonym = synonym

    def as_tuple(self):
        return self.id, self.common_name, self.synonym

    def __repr__(self):
        return f'\'{self.common_name}\' -- Synonym:{self.id}'

def clean(to_clean):
    to_clean = to_clean.strip()
    to_clean = str.lower(to_clean)
    return to_clean

class DrugIndex:
    def __init__(self, synonym_dict, common_name_dict, df):
        self.indexed_synonyms = synonym_dict
        self.common_names = common_name_dict
        self.drug_bank_df = df

    def normalise_drug(self, name):
        if self.common_names.get(name) is not None:
            return name
        if self.indexed_synonyms.get(name) is not None:
            return self.indexed_synonyms.get(name).common_name
        else:
            return None

    @staticmethod
    def init_with_drugbank():
        df = pd.read_csv(drugbank_data_file)

        synonym_dict = {}
        common_name_dict = {}
        for index, row in df.iterrows():
            common_name = clean(row["Common name"])
            common_name_dict[common_name] = row.astype(str).apply(clean)
            pipe_separated_synonyms = str(row["Synonyms"])
            for synonym in pipe_separated_synonyms.split("|"):
                synonym = clean(synonym)
                synonym_dict[synonym] = Synonym(row["DrugBank ID"], common_name, synonym)

        print(f"Loaded drug index with {len(synonym_dict)} synonyms")
        return DrugIndex(synonym_dict, common_name_dict, df)

    @staticmethod
    def get_drug_index():
        return drug_index

drug_index = DrugIndex.init_with_drugbank()



class CleanedDBDrug:
    def __init__(self, db_identifier, drug_name):
        self.db_identifier = str(db_identifier)
        self.cleaned_name = clean(str(drug_name))
        if self.cleaned_name is not None:
            self.synonym = drug_index.indexed_synonyms.get(self.cleaned_name)
            self.common_name = drug_index.normalise_drug(self.cleaned_name)
        else:
            print(f"cleaning removed all info for {db_identifier} [{drug_name}]")

    def __repr__(self):
        return f'\'{self.db_identifier}\' -- cleaned_db_name:{self.cleaned_name} -- common_name:{self.common_name} -- synonym:{self.synonym.synonym if self.synonym is not None else None }'

    def get_norm_name(self):
        if self.synonym is not None:
            return self.synonym.common_name
        else:
            return self.cleaned_name

def index_mimic_drugs(df, id_col='item_id', drug_name_col='label'):

    mimic_drugs_by_norm_name = {}
    for index, row in df.iterrows():
        db_identifier = row[id_col]
        drug_name = row[drug_name_col]
        cleaned_drug = CleanedDBDrug(db_identifier, drug_name)
        mimic_drugs_by_norm_name[cleaned_drug.get_norm_name()] = cleaned_drug
    return mimic_drugs_by_norm_name
#%%

#%%
