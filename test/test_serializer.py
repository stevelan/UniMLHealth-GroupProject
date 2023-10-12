# test_serializer.py - test of serializer.py
import unittest

from detectdd import serializer
from os.path import exists

from detectdd.config import out_dir, cohort_out_file


class SerializerTestCase(unittest.TestCase):
    test_obj = {'key', 'value'}
    def test_serialize(self):
        serializer.write_cohort(self.test_obj)
        self.assertTrue(exists(cohort_out_file), str(cohort_out_file) + " does not exist")

    def test_deserialize(self):
        serializer.write_cohort(self.test_obj)
        deserialized_obj = serializer.read_cohort()
        self.assertEquals(self.test_obj, deserialized_obj)


if __name__ == '__main__':
    unittest.main()

#%%
