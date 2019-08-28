import unittest
from datastructures.algorithm.bubble import bubble_sort


class BubbleSortTest(unittest.TestCase):

    def setUp(self):
        self.array = list(reversed(range(1, 10)))

    def test_should_be_callable(self):
        self.assertTrue(callable(bubble_sort))
    
    def test_should_sort_from_lower_to_great(self):
        self.assertEqual(list(range(1, 10)), bubble_sort(self.array))