
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
    
    def test_solution_two(self):
        nums1 = [2, 3, 5]
        nums2 = [1, 1]
        m = 3
        n = 2
        result = self.obj.merge(nums1=nums1, nums2=nums2, m=m, n=n)
        self.assertEqual(result,[1, 1, 2, 3, 5])
    
    def test_solution_three(self):
        nums1 = [2, 3, 5]
        nums2 = [1]
        m = 2
        n = 1
        result = self.obj.merge(nums1=nums1, nums2=nums2, m=m, n=n)
        self.assertEqual(result,[1, 2, 3])
    
    def test_solution_four(self):
        nums1 = [2, 3, 5]
        nums2 = [1]
        m = 2
        n = 0
        result = self.obj.merge(nums1=nums1, nums2=nums2, m=m, n=n)
        self.assertEqual(result,[2, 3])
    
    def test_solution_five(self):
        nums1 = [2, 3, 5]
        nums2 = []
        m = 2
        n = 0
        result = self.obj.merge(nums1=nums1, nums2=nums2, m=m, n=n)
        self.assertEqual(result,[2, 3])