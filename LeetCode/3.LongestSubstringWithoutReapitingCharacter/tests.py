
import unittest

from longestSubstringWithoutRepetion import  LongestSubstring


class Solution(unittest.TestCase):
    def setUp(self):
        self.obj = LongestSubstring()
    

    def test_longest_substring_one(self):
        data = "abcabcbb"
        result = self.obj.longString(s=data)
        self.assertEqual(result, 3)
    
    def test_longest_substring_two(self):
        data = "pwwkew"
        result = self.obj.longString(s=data)
        self.assertEqual(result, 3)
    