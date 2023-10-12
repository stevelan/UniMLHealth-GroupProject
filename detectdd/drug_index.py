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

class DrugIndex:
    def __init__(self, synonym_dict, common_name_dict):
        self.indexed_synonyms = synonym_dict
        self.common_names = common_name_dict

    def normalise_drug(self, name):
        if self.common_names.get(name) is not None:
            return self.common_names.get(name)
        elif self.indexed_synonyms.get(name) is not None:
            return self.indexed_synonyms.get(name)
        else:
            return name

    @staticmethod
    def init_with_drugbank():
        df = pd.read_csv(drugbank_data_file)

        synonym_dict = {}
        common_name_dict = {}
        for index, row in df.iterrows():
            common_name = row["Common name"]
            common_name_dict[common_name] = row
            pipe_separated_synonyms = str(row["Synonyms"])
            for synonym in pipe_separated_synonyms.split("|"):
                synonym_dict[synonym] = Synonym(row["DrugBank ID"], common_name, synonym)

        print(f"Loaded drug index with {len(synonym_dict)} synonyms")
        return DrugIndex(synonym_dict, common_name_dict)
