
import unittest

from regularExpressionMatching import RegularExpressionMatching as RegEx


class Solution(unittest.TestCase):
	def setUp(self):
		self.obj = RegEx()
	
	def test_RegEx_one(self):
		s = "jove"
		p = "jove"
		result = self.obj.matche(s, p)
		self.assertEqual(result, True)
