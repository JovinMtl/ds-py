
import unittest

from ZigzagConversion import ZigzagConversion


class ZigzagConversionTest(unittest.TestCase):
    def setUp(self):
        self.obj = ZigzagConversion()
    
    def test_zigzag_one(self):
        data = "PAYPALISHIRING"
        result = self.obj.convert(data=data, numRows=4)
        self.assertEqual(result, "PINALSIGYAHRPI")
    
    def test_zigzag_two(self):
        data = "PAYPALISHIRING"
        result = self.obj.convert(data=data, numRows=3)
        self.assertEqual(result, "PAHNAPLSIIGYIR")
    
    def test_zigzag_three(self):
        data = "ABCDE"
        result = self.obj.convert(data=data, numRows=3)
        self.assertEqual(result, "AEBDC")
    
    def test_zigzag_four(self):
        data = "ABCDEF"
        result = self.obj.convert(data=data, numRows=3)
        self.assertEqual(result, "AEBDFC")

    
    def test_zigzag_five(self):
        data = "ABCDEF"
        result = self.obj.convert(data=data, numRows=1)
        self.assertEqual(result, "ABCDEF")

    
    def test_zigzag_six(self):
        data = "ABC"
        result = self.obj.convert(data=data, numRows=2)
        self.assertEqual(result, "ACB")