

class LongestPalindromicSubstring:

    def solution(self, data):
        l_d = len(data)
        i = 1
        longest = ''
        if data == data[::-1]:
            if len(data) > len(longest):
                longest = data
        while i < (l_d-1):
            m1 = data[i:] # taking the first caracter to match the rest
            if m1 == m1[::-1]:
                if len(m1) > len(longest):
                    longest = m1
            j = 1
            while j <= (l_d-1): # the rest to match with, or m1 to be the next
                m2 = data[:-j]
                m3 = data[i:-j]
                if m2 == m2[::-1] and \
                    len(m2)>1 and (len(m2) > len(longest)):
                    longest = m2
                elif m3 == m3[::-1] and \
                    len(m3)>1 and len(m3)> len(longest):
                    longest = m3
                j += 1
            i += 1
        if (data[0]) > longest:
            longest = data[0]
        return longest
