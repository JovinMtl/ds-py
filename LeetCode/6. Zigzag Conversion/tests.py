
import unittest

from ZigzagConversion import ZigzagConversion


class ZigzagConversionTest(unittest.TestCase):
    def setUp(self):
        self.obj = ZigzagConversion()
    
    # def test_zigzag_one(self):
    #     data = "PAYPALISHIRING"
    #     result = self.obj.convert(data=data, numRows=3)
    #     self.assertEqual(result, "PINALSIGYAHRPI")
    
    def test_zigzag_two(self):
        data = "ABCDE"
        result = self.obj.convert(data=data, numRows=3)
        self.assertEqual(result, "AEBDC")
    
    def test_zigzag_three(self):
        data = "ABCDEF"
        result = self.obj.convert(data=data, numRows=3)
        self.assertEqual(result, "AEBDFC")