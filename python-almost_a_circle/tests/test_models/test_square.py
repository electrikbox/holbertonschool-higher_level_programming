#!/usr/bin/python3
""" Unittest for Square class """

import unittest

from models.rectangle import Rectangle
from models.square import Square
from tests.test_models.test_rectangle import TestRectangle


class TestSquare(TestRectangle):
    """ Testing Square class """

    # INHERITANCE --------------------------------------------------------

    def test_inheritance(self):
        """test inheritance"""
        super().test_inheritance()

    # AREA ---------------------------------------------------------------

    def test_area(self):
        """Test area"""
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_area_large(self):
        """Test large area"""
        square = Square(100)
        self.assertEqual(square.area(), 10000)

    def test_area_zero(self):
        """Test zero area"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_area_str(self):
        """Test str area"""
        with self.assertRaises(TypeError):
            Square("test")

    def test_area_negative(self):
        """Test negative area"""
        with self.assertRaises(ValueError):
            Square(-5)


if __name__ == '__main__':
    unittest.main()
