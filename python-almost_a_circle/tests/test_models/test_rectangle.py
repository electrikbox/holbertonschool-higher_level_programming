#!/usr/bin/python3
""" Unittest for Rectangle class """

import unittest

from tests.test_models.test_base import TestBase
from models.rectangle import Rectangle


class TestRectangle(TestBase):
    """ Testing Rectangle class """

    def test_valid_attributes(self):
        rect = Rectangle(10, 20, 5, 5)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 5)

    """ Testing invalid attributes """

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 20, 5, 5)
        with self.assertRaises(ValueError):
            Rectangle(-10, 20, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle(None, 20, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle("hello", 20, 5, 5)

    def test_area(self):
        """ Testing area """
        rect = Rectangle(10, 20, 5, 5)
        self.assertEqual(rect.area(), 200)

    def test_area_large(self):
        """ Testing large area """
        rect = Rectangle(1000, 2000, 500, 500)
        self.assertEqual(rect.area(), 2000000)

    def test_area_zero(self):
        """ Testing zero area """
        with self.assertRaises(ValueError):
            Rectangle(0, 20, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 0, 0, 0)


if __name__ == '__main__':
    unittest.main()