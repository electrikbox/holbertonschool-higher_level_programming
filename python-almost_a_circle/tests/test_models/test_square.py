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
        self.assertTrue(issubclass(Square, Rectangle))


if __name__ == '__main__':
    unittest.main()
