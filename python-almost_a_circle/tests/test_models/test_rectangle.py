#!/usr/bin/python3
""" Unittest for Rectangle class """

import unittest

from models.base import Base
from models.rectangle import Rectangle
from tests.test_models.test_base import TestBase

from io import StringIO
from contextlib import redirect_stdout


class TestRectangle(TestBase):
    """ Testing Rectangle class """

    # INHERITANCE --------------------------------------------------------

    def test_inheritance(self):
        """test inheritance"""
        self.assertTrue(issubclass(Rectangle, Base))

    # ATTRIBUTS ----------------------------------------------------------

    def test_valid_attributes(self):
        """test attributs"""
        rect = Rectangle(10, 20, 5, 5)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 5)

    def test_invalid_width(self):
        """test invalid attributs"""
        with self.assertRaises(ValueError):
            Rectangle(0, 20, 5, 5)
        with self.assertRaises(ValueError):
            Rectangle(-10, 20, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle(None, 20, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle("hello", 20, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle(3.14, 20, 5, 5)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            Rectangle(20, 0, 5, 5)
        with self.assertRaises(ValueError):
            Rectangle(20, -20, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle(20, 3.14, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle(20, "hello", 5, 5)
        with self.assertRaises(TypeError):
            Rectangle(20, 3.14, 5, 5)

    def test_invalid_xy(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -5, 5)
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 5, -5)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 3.14, 5)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 5, 3.14)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, "test", 5)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 5, "test")

    # AREA ---------------------------------------------------------------

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

    def test_area_str(self):
        """Test str area"""
        with self.assertRaises(TypeError):
            Rectangle(10, "test", 0, 0)
        with self.assertRaises(TypeError):
            Rectangle("test", 10, 0, 0)

    def test_area_negative(self):
        """Test negative area"""
        with self.assertRaises(ValueError):
            Rectangle(10, -20, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(-20, 10, 0, 0)

    # DISPLAY ------------------------------------------------------------

    def test_display(self):
        """Test displaying a rectangle in stdout"""
        rect = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with StringIO() as buf, redirect_stdout(buf):
            rect.display()
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

    def test_display_with_xy(self):
        """Test displaying a rectangle in stdout"""
        rect = Rectangle(2, 2, 5, 2)
        expected_output = "\n\n     ##\n     ##\n"
        with StringIO() as buf, redirect_stdout(buf):
            rect.display()
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

    def test_invalid_with_str(self):
        """Test creating a Rectangle with an invalid width"""
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r = Rectangle("invalid", 2, 0, 0)

    def test_invalid_with_0(self):
        """Test creating a Rectangle with an invalid width"""
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r = Rectangle(0, 0, 0, 0)

    # STR ----------------------------------------------------------------

    def test_str(self):
        """Test print rectangle representation in stdout"""
        rect = Rectangle(4, 5, 0, 0)
        expected_output = "[Rectangle] (17) 0/0 - 4/5\n"
        with StringIO() as buf, redirect_stdout(buf):
            print(rect)
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

    def test_str_0(self):
        """Test print 0 size rectangle representation in stdout"""
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(0, 0, 0, 0)

    def test_str(self):
        """Test print invalid rectangle representation in stdout"""
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("test", 5, 0, 0)

    # UPDATE -------------------------------------------------------------

    def test_update_with_args(self):
        """Test update rectangle"""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20, 30, 40, 50)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)
        self.assertEqual(rect.x, 40)
        self.assertEqual(rect.y, 50)
        self.assertEqual(rect.id, 10)

    def test_update_with_partial_args(self):
        """Test update rectangle"""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 10)

    def test_update_with_kwargs(self):
        """Test update rectangle"""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(id=10, height=34, x=2, y=4, width=10)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 34)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 10)

    def test_update_with_partial_kwargs(self):
        """Test update rectangle"""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(id=10, height=34)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 34)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 10)

    def test_update_with_kwargs_value_0(self):
        """Test update rectangle with TypeError and ValueError"""
        rect = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            rect.update(width=0)


if __name__ == '__main__':
    unittest.main()
