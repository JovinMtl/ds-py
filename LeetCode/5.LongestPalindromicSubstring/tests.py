
import unittest

from longestPalindrome import LongestPalindromicSubstring


class Solution(unittest.TestCase):
    def setUp(self):
        self.obj = LongestPalindromicSubstring()
    

    def test_longestPalindrome_one(self):
        data = "aba"
        result = self.obj.solution(data=data)
        self.assertEqual(result, "aba")