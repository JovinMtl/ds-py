
import unittest

from integertoRoman import IntegertoRoman


class Solution(unittest.TestCase):
    def setUp(self):
        self.obj = IntegertoRoman()
    
    def test_integertoRoman_one(self):
        number = 2000
        result = self.obj.toRoman(data=number)
        self.assertEqual(result, "MM")