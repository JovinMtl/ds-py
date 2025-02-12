

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
        print(f"Number after cinq_cent:{number}")
        if cents:
            number -= (cents * 100)
            roman += "C"*cents
        print(f"Number after cents: {number}")
        cinquante = int(number / 50)
        if cinquante:
            number -= (cinquante * 50)
            roman += "L"*cinquante
        if number > 10 and number < 50:
            dix = int(number / 10)
            roman += "X"*(5-dix)
            roman += "L"
            number -= (dix * 10)
        if number == 9:
            number -= 9
            roman += "IX"
        cinq = int(number / 5)
        if cinq:
            number -= (cinq * 5)
            roman += "V"*cinq
        if number:
            roman += "I"*number
        return roman
    