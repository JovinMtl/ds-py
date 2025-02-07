

class ZigzagConversion:
    def convert(self, data:str, numRows:int=1)->str:
        if numRows == 1:
            return data
        arr = []
        i = 0
        t = 0
        while i < numRows:
            if t == len(data):
                break
            arr.append([])
            arr[i].append(data[t])
            t += 1
            if i == (numRows - 1) and (t < len(data)):
                j = numRows - 2
                while j >= 0:
                    arr[j].append(data[t])
                    j -= 1
                    t += 1
            i += 1
            if (i == numRows) and (t < len(data)):
                i = 1
        return self._compact(arr)
    
    def _compact(self, data:list)->str:
        result = ""
        for dat in data:
            result += self._assemb(data=dat)
        return result
    def _assemb(self, data:list)->str:
        result = ""
        for dat in data:
            result += dat
        return result