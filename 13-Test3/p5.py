class C():
    def __init__(self,imie,nazw,wiek,staz):
        self.imie = imie
        self.nazw = nazw
        self.wiek = wiek
        self.staz = staz
    def __str__(self):
        result = ""
        result += self.imie[0]
        result += self.nazw
        result += str(self.wiek)
        if self.staz >= 5:
            result += "+"
        return result