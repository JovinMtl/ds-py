

class LongestSubstring:
    def longString(self, s: str) -> int:
        if len(s) <= 0 and len(s) <= 5 * (10**4):
            return 0
        longest = 0
        combined = ''
        i = 0
        j = 1
        while i < len(s):
            if s[i] in combined:
                index = (combined.index(s[i])) + 1
                combined = combined[index:] + s[i]
            else:
                combined += s[i]

            if len(combined) > longest:
                longest = len(combined)
            i += 1
        
        return longest
        