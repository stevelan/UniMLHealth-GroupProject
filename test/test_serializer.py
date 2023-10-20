# test_serializer.py - test of serializer.py
import unittest
from os.path import exists

from detectdd.config import cohort_fast_out_file
from detectdd.serializer import Serializer


class SerializerTestCase(unittest.TestCase):
    test_obj = {'key', 'value'}
    serializer = Serializer()

    def test_serialize(self):
        self.serializer.write_cohort(self.test_obj)
        self.assertTrue(exists(cohort_fast_out_file), str(cohort_fast_out_file) + " does not exist")

    def test_deserialize(self):
        self.serializer.write_cohort(self.test_obj)
        deserialized_obj = self.serializer.read_cohort()
        self.assertEqual(self.test_obj, deserialized_obj)


if __name__ == '__main__':
    unittest.main()

# %%
