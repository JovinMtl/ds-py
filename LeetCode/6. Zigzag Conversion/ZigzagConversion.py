
 
class ZigzagConversion:
    def convert(self, data:str, numRows:int=1)->str:
        arr = []
        i = 0
        t = 0
        print(f"With len of {len(data)}: {data}")
        while i < numRows:
            if t == len(data):
                break
            arr.append([])
            print(f"Consider: i{i}, index:{t}, value:{data[t]}")
            arr[i].append(data[t])
            t += 1
            if i == (numRows - 1):
                j = numRows - 2
                while j >= 0:
                    arr[j].append(data[t])
                    j -= 1
                    t += 1
            i += 1
            if (i == numRows) and (t < len(data)):
                i = 1
        return arr