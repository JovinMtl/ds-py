import unittest
from roundingNumber import RoundNumber

class Test(unittest.TestCase):
    def setUp(self):
        self.obj = RoundNumber()
    

    def test_longest_substring_one(self):
        data = 830
        result = self.obj.round(val=data)
        self.assertEqual(result, 800)

    def test_longest_substring_two(self):
        data = 1120
        result = self.obj.round(val=data)
        self.assertEqual(result, 1500)

