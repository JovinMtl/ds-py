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

    def test_longest_substring_three(self):
        data = 5220
        result = self.obj.round(val=data)
        self.assertEqual(result, 5500)

    def test_longest_substring_three(self):
        data = 10300
        result = self.obj.round(val=data)
        self.assertEqual(result, 11000)

    def test_longest_substring_four(self):
        data = 21250
        result = self.obj.round(val=data)
        self.assertEqual(result, 22000)

    def test_longest_substring_five(self):
        data = 260
        result = self.obj.round(val=data)
        self.assertEqual(result, 300)

    def test_longest_substring_five(self):
        data = 1720
        result = self.obj.round(val=data)
        self.assertEqual(result, 2000)

