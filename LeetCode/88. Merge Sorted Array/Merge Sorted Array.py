class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cond1 = len(nums1) == m + n
        cond2 = len(nums2) == n
        cond3 = 0 <= m and n <= 200
        cond4 = 1 <= m + n <= 200
        cond5 = (-109 <= nums1[m-1]) and (nums2[n-1] <= 109)
        worth = False
        once = True

        if cond1 and cond2 and cond3 and \
            cond4 and cond5:
            worth = True
        
        if worth:
            max = m + n
            i = 0
            arr = []
            i1, i2 = 0, 0
            while (i < max):
                print((i2 < (n)))
                if nums1[i1] < nums2[i2]:
                    arr.append(nums1[i1])
                    i1 += 1
                else:
                    print(f"i2: {i2} = {nums2[i2]}")
                    arr.append(nums2[i2])
                    i2 += 1
                if (i2 >= n) and once:
                    print(f"ONLY HERE")
                    nums2.append(self._makePos(nums1[i1]+1))
                    # once = False
                i += 1
            nums1 = arr
        else:
            print(f"Not worthy:{cond1}{cond2}{cond3}{cond4}{cond5}")
        
        print(f"The nums1 ends with {nums1}")
    
    def _makePos(self, num)->int:
        if num < 0:
            return num * -1
        else:
            return num


obj = Solution().merge([1,2,8,5,6],3, [0,1], 2)