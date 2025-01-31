
import unittest

from MergeSortedArray import Solution


class TestMergeSortedArray(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_solution_one(self):
        nums1 = [ 0, 1, 2, 3, 5]
        nums2 = [1, 1]
        m = 3
        n = 2
        result = self.obj.merge(nums1=nums1, nums2=nums2, m=m, n=n)
        self.assertEqual(result,[0, 1, 1, 1, 2])