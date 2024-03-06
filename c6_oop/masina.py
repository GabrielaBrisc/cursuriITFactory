# o clasa este o schita a unei realitati din lumea reala

class Masina:
    # atribute default
    marca = None
    model = None
    culoare = "alb"
    motor_pornit = False
    viteza = 0

    #constructor - o met care ne obliga sa dam ca valori parametrilor
    # mentionati intre () atunci cand cream obiecte
    #acesta ne obliga sa folosim atributele specificate
    def __init__(self, marca, model):
        #self.marca este atributul obiectului instantiat
        #marca este param functiei, prin el va veni valoarea pe care o dam
        #cand cream obiectul
        self.marca = marca
        self.model = model

        # metoda
    def prezentare_masina(self):
        #cream o variabila
        if self.motor_pornit: # echiv cu self.motor_pornit == True
            stare_motor = "pornit"
        else:
            stare_motor = "oprit"
        print(f"Masina {self.marca}, cu modelul {self.model}, are culoarea {self.culoare}"
              f" si are motorul {stare_motor} "
              f"cu viteza de {self.viteza} km/h")
    def start(self):
        self.motor_pornit = True

    def stop(self):
        self.motor_pornit = False
        self.viteza = 0

    def accelereaza(self, valoare_accelerare):
        if self.motor_pornit == True: # <=> self.motor_pornit
            self.viteza += valoare_accelerare
            print(f"masina a ajuns la {self.viteza} km/h")
        else:
            print("nu se poate accelera deoarece nu este pornit motorul")

    def incetineste(self, incetineste_cu):
        if self.motor_pornit == True and self.viteza > 0:
            if self.viteza > incetineste_cu:
                self.viteza -= incetineste_cu
            else:
                 self.viteza = 0
            print(f"masina a ajuns la {self.viteza} km/h")
        else:
            print("Nu putem incetini pt ca motorul nu este pornit sau viteza este deja 0")


# instantiem un obiect de tip Masina()
# in acest mod o sa avem access la toate atributele din cls Masina
# masina_1 = Masina()
# print(masina_1.model)
# print(masina_1.culoare)

#modificam un atribut
# masina_1.model = "R7"
# print(masina_1.model)

# alt obiect
# masina_2 = Masina()
# print(masina_2.model)

