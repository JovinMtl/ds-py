
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