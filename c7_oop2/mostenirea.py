### Inheritance ###

# Clasa parinte:
class Persoana:
    def __init__(self, nume, varsta, adresa):
        self.nume =nume
        self.varsta = varsta
        self.adresa = adresa

    def descriere(self):
        print("-"*50)
        print(f"Nume: {self.nume}",
              f"Varsta: {self.varsta} ani",
              f"Adresa: {self.adresa}")

    def anul_nasterii(self):
        return 2024 - self.varsta

# Clasa copil
class Student(Persoana):
    #constructor
    def __init__(self, nume, varsta, adresa, facultate, an_studiu):
        #super reprezinta clasa parinte
        #accesam constructorul din cls parinte (Persoana)
        super().__init__(nume, varsta, adresa)
        self.facultate = facultate
        self.an_studiu = an_studiu

    def descriere(self):
        super().descriere()
        print(f"Facultate: {self.facultate}",
              f"an studiu: {self.an_studiu}")

class Angajat(Persoana):
    def __init__(self, nume, varsta, adresa,companie,salariu):
        super().__init__(nume, varsta, adresa)
        self.companie =companie
        self.salariu = salariu

    def descriere(self):
        super().descriere()
        print(f"Companie: {self.companie}",
              f"Salariu: {self.salariu} lei")

    def salariu_anual(self):
        return self.salariu * 12

#clasa copil care mosteneste o clasa copil, care la randul ei a mostenit clasa parinte

class Profesor(Angajat):
    def __init__(self, nume, varsta, adresa, companie, salariu, curs, nr_ore):
        super().__init__(nume, varsta, adresa, companie, salariu)
        self.curs = curs
        self.nr_ore =nr_ore
    def descriere(self):
        super().descriere()
        print(f"Curs: {self.curs}",
              f"Numar ore: {self.nr_ore}")