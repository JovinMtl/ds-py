

class LongestPalindromicSubstring:

    def solution(self, data):
        l_d = len(data)
        i = 1
        solutions = []
        if data == self._re(data):
            solutions.append(data)
            # return data
        while i < (l_d-1):
            m1 = data[i:] # taking the first caracter to match the rest
            if self._re(m1) == m1:
                solutions.append(m1)
                # return m1
            j = 1
            while j <= (l_d-1): # the rest to match with, or m1 to be the next
                m2 = data[:-j]
                m3 = data[i:-j]
                if self._re(m2) == m2 and \
                    len(m2)>1:
                    solutions.append(m2)
                    # return m2
                elif self._re(m3) == m3 and \
                    len(m3)>1:
                    solutions.append(m3)
                    # return m3
                j += 1
            i += 1
        solutions.append(data[0])
        longest = ''
        print(f"We have {len(solutions)} solutions")
        for solution in solutions:
            if len(solution) > len(longest):
                longest = solution
        return longest
    
    def _re(self, data):
        # This method is for reversing the string
        l_d = len(data) - 1
        i = 0
        result = ''
        while l_d >= 0:
            result += data[l_d]
            l_d -= 1
        return result
