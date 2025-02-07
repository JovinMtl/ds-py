

class IntegertoRoman:
    def toRoman(self, data:int)->str:
        number = data
        roman = ""
        milles = int(number / 1000)
        if milles:
            number -= (milles * 1000)
            roman += "M"*milles
        cinq_cent = int(number / 500)
        if cinq_cent:
            number -= (cinq_cent * 500)
            roman += "D"*cinq_cent
        cents = int(number / 100)
        if cents:
            number -= (cents * 100)
            roman += "C"*100
        cinquante = int(number / 50)
        if cinquante:
            number -= (cinquante * 50)
            roman += "L"*cinquante
        dix = int(number / 10)
        if dix:
            number -= (dix * 10)
            roman += "X"*dix
        cinq = int(number / 5)
        if cinq:
            number -= (cinq * 5)
            roman += "V"*cinq
        if number:
            roman += "I"*number
        return roman
    