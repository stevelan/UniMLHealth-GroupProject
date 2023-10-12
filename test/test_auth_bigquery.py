import unittest

from detectdd.auth_bigquery import BigQueryClient



class AuthBigQueryTestCase(unittest.TestCase):
    def test_connect(self):
        mimic_query = """SELECT * FROM `physionet-data.mimiciv_hosp.d_icd_diagnoses` LIMIT 5"""
        df = BigQueryClient.auth().query(mimic_query).to_dataframe()
        self.assertEqual(len(df), 5)  # add assertion here


if __name__ == '__main__':
    unittest.main()

#%%
