
import unittest

from palindromeNumber import PalindromeNumber


class Solution(unittest.TestCase):
    def setUp(self):
        self.obj = PalindromeNumber()
    
    def test_palindromeNumber_one(self):
        number = 120
        result = self.obj.check(data=number)
        self.assertEqual(result, False)
    
    def test_palindromeNumber_two(self):
        number = 121
        result = self.obj.check(data=number)
        self.assertEqual(result, True)
