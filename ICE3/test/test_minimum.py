# Name: Rob Savoie
# Date: Oct 24, 2022
# Project: ICE 3 Unit Testing

import unittest

from ICE3.app.minimum import Minimum


class TestMinimum(unittest.TestCase):
    def setUp(self):
        self.min = Minimum()

    def tearDown(self):
        print("\n End of Test - ", self.shortDescription())

    def test_minimum_short_list_result(self):
        """Test Case 1: A very short list (of inputs) with the size of 1, 2, or 3 elements."""
        numbers = [36, 14, 12]
        self.assertEqual(12, self.min.minimum_number(numbers))

    def test_minimum_empty_list(self):
        """Test Case 2: An empty list i.e., of size 0."""
        numbers = []
        self.assertRaises(TypeError, self.min.minimum_number(numbers))

    def test_minimum_last_element(self):
        """Test Case 3: A list where the minimum element is the first or last element."""
        numbers = [97, 81, 34, 23, 10]
        self.assertEqual(10, self.min.minimum_number(numbers))

    def test_minimum_negative(self):
        """Test Case 4: A list where the minimum element is negative."""
        numbers = [10, -2, 5, 23]
        self.assertEqual(-2, self.min.minimum_number(numbers))

    def test_minimum_all_negative(self):
        """Test Case 5: A list where all elements are negative."""
        numbers = [-23, -31, -45, -56]
        self.assertEqual(-56, self.min.minimum_number(numbers))

    def test_minimum_real_numbers(self):
        """Test Case 6: A list where some elements are real numbers."""
        numbers = [23, 34.56, 67, 33]
        self.assertRaises(TypeError, self.min.is_integer())
        self.assertEqual(23, self.min.minimum_number(numbers))

    def test_minimum_alpha(self):
        """Test Case 7: A list where some elements are alphabetic characters and special characters."""
        numbers = [23, "hi", 32, 1]
        self.assertRaises(TypeError, self.min.minimum_number(numbers))
        self.assertEqual(1, self.min.minimum_number(numbers))

    def test_minimum_duplicate(self):
        """Test Case 8: A list with duplicate elements."""
        numbers = [13, 6, 6, 9, 15]
        self.assertEqual(6, self.min.minimum_number(numbers))

    def test_minimum_beyond_max(self):
        """Test Case 9: A list where one element has a value greater than the maximum permissible limit of an integer."""
        numbers = [530, 429449672, 97, 23, 46, 59]
        self.assertEqual(23, self.min.minimum_number(numbers))


if __name__ == '__main__':
    unittest.main()
