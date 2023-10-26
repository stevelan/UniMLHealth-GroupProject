# serializer.py -
import pickle

from detectdd import config


class Serializer:
    def write_cohort(self, cohort):
        filename = self.get_cohort_filename()
        _write_file(cohort, filename)

    def read_cohort(self):
        # Deserialization
        try:
            filename = Serializer.get_cohort_filename()
            return _read_file(filename)
        except FileNotFoundError:
            raise Exception(
                "Need to run [01-cohort.ipynb and 01a-cohorts-icd-codes.ipynb] to create the cohort file [" + str(
                    filename) + "] in the /out directory")

    def write_cohort_with_no_icd(self, cohort):
        _write_file(cohort, config.cohort_no_icd_out_file)

    def read_cohort_with_no_icd(self):
        return _read_file(config.cohort_no_icd_out_file)

    def write_emar_drug_interactions(self, cohort):
        _write_file(cohort, config.emar_interactions_out_file)

    def read_emar_drug_interactions(self):
        return _read_file(config.emar_interactions_out_file)

    def write_icu_drug_interactions(self, cohort):
        _write_file(cohort, config.icu_interactions_out_file)

    def read_icu_drug_interactions(self):
        return _read_file(config.icu_interactions_out_file)

    def write_total_drug_interactions(self, cohort):
        _write_file(cohort, config.total_interactions_out_file)

    def read_total_drug_interactions(self):
        return _read_file(config.total_interactions_out_file)

    @staticmethod
    def get_cohort_filename():
        # if config.isFastMode():
        #     return config.cohort_fast_out_file
        return config.cohort_full_out_file

    def write_bp_results(self, df, suffix=""):
        _write_file(df, config.out_dir / ("bp_results" + suffix + ".out"))

    def read_bp_results(self, suffix=""):
        return _read_file(config.out_dir / ("bp_results" + suffix + ".out"))

def _write_file(cohort, filename):
    with open(filename, "wb") as outfile:
        # "wb" argument opens the file in binary mode
        print("Saved cohort to " + str(filename))
        pickle.dump(cohort, outfile)


def _read_file(filename):
    with open(filename, "rb") as infile:
        deserialized = pickle.load(infile)
    print("Loaded cohort from " + str(filename))
    return deserialized

# %%
