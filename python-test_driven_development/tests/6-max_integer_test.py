#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_regular(self):
        """Test with a regular list of ints"""
        test_list = [1, 2, 3, 4, 5, 6, 7, 8]
        result = max_integer(test_list)
        self.assertEqual(result, 8)

    def test_float(self):
        """Test with a regular list of floats"""
        test_list = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8]
        result = max_integer(test_list)
        self.assertEqual(result, 8.8)

    def test_negative_int(self):
        """Test with a negative list of ints"""
        test_list = [-1, -2, -3, -4, -5, -6, -7, -8]
        result = max_integer(test_list)
        self.assertEqual(result, -1)

    def test_negative_float(self):
        """Test with a regular list of floats"""
        test_list = [-1.1, -2.2, -3.3, -4.4, -5.5, -6.6, -7.7, -8.8]
        result = max_integer(test_list)
        self.assertEqual(result, -1.1)

    def test_word(self):
        """Test with a list of words"""
        test_list = ["Hello", "World", "!"]
        result = max_integer(test_list)
        self.assertEqual(result, "World")

    def test_bool(self):
        """Test with a list of booleans"""
        test_list = [True, False, True]
        result = max_integer(test_list)
        self.assertEqual(result, True)

    def test_matrix(self):
        """Test with a list of matrices"""
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = max_integer(test_list)
        self.assertEqual(result, [7, 8, 9])

    def test_all_values_equal(self):
        """Test with a list of all values equal"""
        test_list = [1, 1, 1, 1, 1, 1, 1, 1]
        result = max_integer(test_list)
        self.assertEqual(result, 1)

    def test_empty_list(self):
        """Test with an empty list"""
        test_list = []
        result = max_integer(test_list)
        self.assertEqual(result, None)

    def test_one_element(self):
        """Test with a list of one element"""
        test_list = [1]
        result = max_integer(test_list)
        self.assertEqual(result, 1)

    def test_string(self):
        """Test with a string"""
        test_list = "Hello"
        result = max_integer(test_list)
        self.assertEqual(result, "o")

    def test_infinity(self):
        """Test with a list of infinite values"""
        test_list = [float('inf'), float('-inf')]
        result = max_integer(test_list)
        self.assertEqual(result, float('inf'))

    def test_is_None(self):
        """Test with a None value"""
        test_list = [None]
        result = max_integer(test_list)
        self.assertIsNone(result)

    def test_none(self):
        """Test with a None value"""
        self.assertRaises(TypeError, max_integer, None)

    def test_arg_True(self):
        """Test with no argument"""
        self.assertRaises(TypeError, max_integer, True)

    def test_too_many_args(self):
        """Test with too many arguments"""
        self.assertRaises(TypeError, max_integer, 1, 2, 3)

    def test_not_iterable(self):
        """Test with a non-iterable"""
        self.assertRaises(TypeError, max_integer, 1)

    def test_dict(self):
        """Test with a dictionary"""
        self.assertRaises(KeyError, max_integer, {"a": 1, "b": 2})

    def test_different_types(self):
        """Test with a list of mixed types"""
        self.assertRaises(TypeError, max_integer, [1, 2, 3], "Hello")

    def test_duplicate_values(self):
        """Test with a list of different types"""
        self.assertRaises(TypeError, max_integer, [True, 10, "Hello"])


if __name__ == '__main__':
    unittest.main()
