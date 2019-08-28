import unittest
from datastructures.algorithm.binary_search import binary_search


class BubbleSortTest(unittest.TestCase):

    def setUp(self):
        self.array = list(range(0, 1000))

    def test_should_be_callable(self):
        self.assertTrue(callable(binary_search))
    
    def test_should_found_0_in_the_index_0(self):
        self.assertEqual(0, binary_search(self.array, 0))

    def test_should_found_999_in_the_index_999(self):
        self.assertEqual(999, binary_search(self.array, 999))
    
    def test_should_not_found_2000_and_return_minus_one(self):
        self.assertEqual(-1, binary_search(self.array, 2000))