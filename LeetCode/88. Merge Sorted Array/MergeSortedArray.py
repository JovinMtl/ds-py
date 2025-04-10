class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        has_left = True # will compound the left list when empty
        if (len(nums1)> m):
            nums1 = nums1[:m]
        if (len(nums1) < m) and (len(nums2) < n):
            has_left = False
        if len(nums1)==0 and len(nums2)==0:
            has_left = False
        if m == 0 and n and has_left:
            nums1 = nums2[:n] #put all on the left
            has_left = False # avoid the left
        if len(nums1) < m and has_left:
            m = len(nums1)
            nums1 = nums1[:m]
        if not (len(nums1) == m + n) and has_left:
            a = len(nums1)
            while a < m + n:
                nums1.append(nums1[a-1]*10)
                a += 1
        if (not n) and (m < len(nums1)):
            nums1 = nums1[:m]
        cond1 = len(nums1) == m + n
        cond2 = len(nums2) == n
        cond3 = 0 <= m and n <= 200
        cond4 = 1 <= m + n <= 200
        cond5 = True
        if not n and len(nums2) and has_left:
            cond2 = True
            cond5 = (-109 <= nums1[m-1]) and (nums2[n-1] <= 109)
        if (len(nums2)== 0):
            cond5 = False
        worth = False
        once = True
        
        if cond1 and cond2 and cond3 and \
            cond4 and cond5 and has_left:
            worth = True
        
        if worth and n and cond1:
            max = m + n
            i = 0
            arr = []
            i1, i2 = 0, 0
            while (i < max):
                if nums1[i1] < nums2[i2] or  (nums2[i2] is False):
                    arr.append(nums1[i1])
                    i1 += 1
                else:
                    arr.append(nums2[i2])
                    i2 += 1
                if (i2 >= n) and once:
                    nums2.append(False)
                i += 1
            nums1 = arr
        else:
            pass
            # print(f"Not worthy:{cond1}{cond2}{cond3}{cond4}{cond5}")
        
        return nums1


obj = Solution().merge([1,2,8,5,6],3, [0,1], 2)