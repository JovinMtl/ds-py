

class PalindromeNumber:
    def check(self, data:int)->bool:
        data_str = str(data)
        if data_str == data_str[::-1]:
            return True
        return False