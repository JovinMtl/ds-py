
import unittest

from StringtoInteger import StringtoInteger


class TestStringtoInteger(unittest.TestCase):
    def setUp(self):
        self.obj = StringtoInteger()
    
    def test_one(self):
        s = "1"
        self.assertEqual(self.obj.convert(s), 1)