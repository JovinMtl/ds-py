
class StringtoInteger:
    def convert(self, s)->int:
        """will do the job"""
        len_int = len(s)
        is_neg = False
        i = 0
        if s[i] == '-':
            is_neg = True
            i = 1
        elif s[i] == '+':
            i = 1
        digits = []
        while i < len_int:
            try:
                type(int(s[i]))
            except ValueError:
                break
            else:
                digits.append(int(s[i]))
            i += 1
        len_digit = len(digits)
        result = 0
        for digit in digits:
            result += digit * (10**(len_digit-1))
            len_digit -= 1
        if is_neg:
            result *= -1
        return result