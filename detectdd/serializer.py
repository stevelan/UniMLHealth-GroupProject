# serializer.py -
import pickle

from detectdd.config import cohort_out_file

test_dict = {"Hello": "World!"}
class Serializer:

    def write_cohort(self, cohort):
        with open(cohort_out_file, "wb") as outfile:
            # "wb" argument opens the file in binary mode
            print("Saved cohort")
            pickle.dump(cohort, outfile)
    def read_cohort(self):
        # Deserialization
        with open(cohort_out_file, "rb") as infile:
            deserialized = pickle.load(infile)
        print("Loaded cohort")
        return deserialized


#%%
