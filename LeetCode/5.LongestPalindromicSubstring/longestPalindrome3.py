

class LongestPalindromicSubstring:
    """
    data = "babad"
    result = "aba"
    """

    def solution(self, data):
        t = '#'.join(f'^{data}$')
        n = len(t)
        P = [0] * n
        C = R = 0

        for i in range(2, n-2):
            # Find the corresponding letter in the palindrome substring
            mirr = 2*C - i
            print(f'{mirr= }, {R= }, {i= }')
            if R > i: P[i] = min(R - i, P[mirr])
            
            # Expand around i
            while t[i + P[i] + 1] == t[i - P[i] - 1]: P[i] += 1
            
            # If palindrome centered at i expands past R, adjust center C and R
            if i + P[i] > R: C, R = i, i + P[i]
        
        max_len, center_index = max((n, i) for i, n in enumerate(P))
        print(P)
        print(list(t))
        start = (center_index - max_len) // 2
        return data[start:start + max_len]
    
# Ran 4 tests in 0.098s