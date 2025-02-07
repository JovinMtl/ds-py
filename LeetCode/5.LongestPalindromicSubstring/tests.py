
import unittest

from longestPalindrome import LongestPalindromicSubstring


class Solution(unittest.TestCase):
    def setUp(self):
        self.obj = LongestPalindromicSubstring()
    

    def test_longestPalindrome_one(self):
        data = "aba"
        result = self.obj.solution(data=data)
        self.assertEqual(result, "aba")

    def test_longestPalindrome_two(self):
        data = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
        result = self.obj.solution(data=data)
        self.assertEqual(result, "ranynar")
        # Took 54.63 sec
        # First on backup took 58.083s
        # Second on backup took 0.740s
    
    def test_longestPalindrome_three(self):
        data = "babad"
        result = self.obj.solution(data=data)
        self.assertEqual(result, "aba")
    

    