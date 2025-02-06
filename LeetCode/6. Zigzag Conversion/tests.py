
import unittest

from ZigzagConversion import ZigzagConversion


class ZigzagConversionTest(unittest.TestCase):
    def setUp(self):
        self.obj = ZigzagConversion()
    
    def test_zigzag_one(self):
        data = "jove"
        result = self.obj.convert(data=data)
        self.assertEqual(result, "jove")