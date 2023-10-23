#!/usr/bin/python3
""" Unittest for Base class """

import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """ Testing instantiation of Base class """

    def test_no_instance_creation(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_None_id(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_instance_creation_with_id(self):
        obj1 = Base(10)
        self.assertEqual(obj1.id, 10)

    def test_negative_id(self):
        self.assertEqual(-5, Base(-5).id)

    def test_float_id(self):
        self.assertEqual(3.14, Base(3.14).id)

    def test_zero_id(self):
        self.assertEqual(0, Base(0).id)


if __name__ == '__main__':
    unittest.main()