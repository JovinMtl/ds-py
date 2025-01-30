class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l_m = len(nums1)
        l_n = len(nums2)
        if not l_n:
            nums2 = [0]
        cond1 = len(nums1) == m + n
        cond2 = len(nums2) == n
        cond3 = 0 <= m and n <= 200
        cond4 = 1 <= m + n <= 200
        cond5 = (-109 <= nums1[m-1]) and (nums2[n-1] <= 109)
        worthy = False

        if cond1 and cond2 and cond3 and \
            cond4 and cond5:
            worth = True
        
        if worthy:
            max = l_m + l_n
            i = 0
            arr = []
            i1, i2 = 0, 0
            while (i2 <= (l_n-1)) and (i1 < (l_m -1)):
                # print(f"i1:{i1} , i2 {i2} out of {l_n}")
                if nums1[i1] < nums2[i2]:
                    # arr.append(nums1[i1])
                    nums1[i] = nums1[i1]
                    i1 += 1
                else:
                    # arr.append(nums2[i2])
                    nums1[i] = nums2[i2]
                    i2 += 1
                i += 1
            # print(f"The arr: {arr}")
            
            # nums1 = arr

        