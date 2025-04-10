

class LongestPalindromicSubstring:
    """
    data = "babad"
    result = "aba"
    """

    def solution(self, data):
        if data == data[::-1]:
            return data
        l_d = len(data)
        i = 1
        j = 1
        longest = data[0]
        while i < (l_d-1):
            m1 = data[i:] # taking the first caracter to match the rest
            if m1 == m1[::-1] and len(m1) > len(longest):
                longest = m1
            m2 = data[(i-j):-j]
            if m2 == m2[::-1] and len(m2) > len(longest):
                longest = m2
            if i == j:
                i += 1
                j = 1
            else:
                j += 1
        return longest
    
# Ran 4 tests in 3.069s
# Ran 4 tests in 0.356s
# Ran 4 tests in 0.404s  successfully
#  seems to have time complexity of O(n**2)