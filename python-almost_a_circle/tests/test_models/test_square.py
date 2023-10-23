#!/usr/bin/python3
""" Unittest for Rectangle class """

import unittest

from models.rectangle import Rectangle
from models.square import Square
from tests.test_models.test_base import TestBase


class TestRectangle(TestBase):
    """ Testing Rectangle class """

    # INHERITANCE --------------------------------------------------------

    def test_inheritance(self):
        """test inheritance"""
        self.assertTrue(issubclass(Square, Rectangle))

    # ATTRIBUTS ----------------------------------------------------------

    def test_valid_attributes(self):
        """test attributs"""
        square = Square(10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertEqual(square.id, 9)


    def test_invalid_attributs(self):
        """test invalid attributs"""
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(TypeError):
            Square(3.14)
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6)


if __name__ == '__main__':
    unittest.main()
