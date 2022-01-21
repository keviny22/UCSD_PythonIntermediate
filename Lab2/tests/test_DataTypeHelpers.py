from unittest import TestCase
from Lab2.Helpers.DataTypeHelpers import isDate, isInt, isFloat

class Test(TestCase):
    def test_is_int_is_True(self):
        response = isInt("1")
        self.assertTrue(response)

    def test_is_int_is_False(self):
        response = isInt("foo")
        self.assertFalse(response)

    def test_is_float_is_True(self):
        response = isFloat("10000000")
        self.assertTrue(response)

    def test_is_float_is_False(self):
        response = isFloat("foo")
        self.assertFalse(response)

    def test_is_date_is_True(self):
        response = isDate("1975-10-27")
        self.assertTrue(response)

    def test_is_date_is_False(self):
        response = isFloat("foo")
        self.assertFalse(response)
