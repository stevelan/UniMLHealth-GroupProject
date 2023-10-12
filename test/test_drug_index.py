import unittest
from detectdd.drug_index import DrugIndex


class DrugIndexTestCase(unittest.TestCase):
    def test_initialise_drug_index(self):
        drug_index = DrugIndex.init_with_drugbank()
        self.assertEqual(34681, len(drug_index.indexed_synonyms), "Should have found synonyms")  # add assertion here


if __name__ == '__main__':
    unittest.main()
