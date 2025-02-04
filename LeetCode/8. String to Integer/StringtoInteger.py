
class StringtoInteger:
    def convert(self, s)->int:
        """will do the job"""
        i = 0
        if len(s)==0:
            return 0
        if s[i] == ' ':
            s = self._removeSpace(s=s)
        if len(s)==0:
            return 0
        len_int = len(s)
        is_neg = False
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
        if result >= (2**31):
            result = (2**31) - 1
        elif result < (-2**31):
            result = -(2**31)
        return result
    
    def _removeSpace(self, s)->str:
        if len(s)==0:
            return ''
        if s[0] == ' ':
            s = s[1:]
            return self._removeSpace(s=s)
        
        return s


# Round "-91283472332" ( -2**31) into  -2147483648