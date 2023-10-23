#!/usr/bin/python3
""" Unittest for Rectangle class """

import unittest

from tests.test_models.test_base import TestBase
from models.rectangle import Rectangle
from io import StringIO
from contextlib import redirect_stdout


class TestRectangle(TestBase):
    """ Testing Rectangle class """

    def test_valid_attributes(self):
        rect = Rectangle(10, 20, 5, 5)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 5)

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
        """Test area"""
        rect = Rectangle(10, 20, 5, 5)
        self.assertEqual(rect.area(), 200)

    def test_area_large(self):
        """Test large area"""
        rect = Rectangle(1000, 2000, 500, 500)
        self.assertEqual(rect.area(), 2000000)

    def test_area_zero(self):
        """Test zero area"""
        with self.assertRaises(ValueError):
            Rectangle(0, 20, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 0, 0, 0)

    def test_display(self):
        """Test displaying a rectangle in stdout"""
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

    def test_display_with_xy(self):
        """Test displaying a rectangle in stdout"""
        r = Rectangle(2, 2, 5, 2)
        expected_output = "\n\n     ##\n     ##\n"
        with StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

    def test_str(self):
        """Test print rectangle representation in stdout"""
        r = Rectangle(4, 5, 0, 0)
        expected_output = "[Rectangle] (17) 0/0 - 4/5\n"
        with StringIO() as buf, redirect_stdout(buf):
            print(r)
            output = buf.getvalue()
            self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()