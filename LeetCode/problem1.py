
data = input("ENter data: ")
class ProbOne:
    def __init__(self, data):
        self.data = data

    def solution(self):
        l_d = len(self.data)
        i = 1
        if self.data == self._re(self.data):
            return self.data
        while i < (l_d-1):
            m1 = self.data[i:] # taking the first caracter to match the rest
            if self._re(m1) == m1:
                return m1
            j = 1
            while j <= (l_d-1): # the rest to match with, or m1 to be the next
                m2 = self.data[:-j]
                m3 = self.data[i:-j]
                if self._re(m2) == m2 and \
                    len(m2)>1:
                    return m2
                elif self._re(m3) == m3 and \
                    len(m3)>1:
                    return m3
                j += 1
            i += 1
        return self.data[0]
    
    def _re(self, data):
        # This method is for reversing the string
        l_d = len(data) - 1
        i = 0
        result = ''
        while l_d >= 0:
            result += data[l_d]
            l_d -= 1
        return result

objOne = ProbOne(data=data)
rep = objOne.solution()

print(f"The Solution from {data} is {rep}")