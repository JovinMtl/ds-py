
import unittest

from StringtoInteger import StringtoInteger


class TestStringtoInteger(unittest.TestCase):
    def setUp(self):
        self.obj = StringtoInteger()
    
    def test_one_string_to_integer(self):
        s = "1"
        self.assertEqual(self.obj.convert(s), 1)

    def test_two_string_to_integer(self):
        s = "23530"
        self.assertEqual(self.obj.convert(s), 23530)

    def test_three_string_to_integer(self):
        s = "   -042"
        self.assertEqual(self.obj.convert(s), -42)

    def test_four_string_to_integer(self):
        s = "-91283472332"
        self.assertEqual(self.obj.convert(s), -2147483648)

    def test_five_string_to_integer(self):
        s = ""
        self.assertEqual(self.obj.convert(s), 0)

    def test_six_string_to_integer(self):
        s = "21474836460"
        self.assertEqual(self.obj.convert(s), 2147483647)

    def test_seven_string_to_integer(self):
        s = " "
        self.assertEqual(self.obj.convert(s), 0)