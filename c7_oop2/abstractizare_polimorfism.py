"""
Abstractizare = este un proces prin care putem sa ascundem o anumita functionalitate specifica de utilizator si de asemenea de a putea forta un anumit omportament in clasele copil
Utilizatorul stie ce face functionalitatea, dar nu si cum

Clasa parinte este o clasa abstracta, deci nu putem sa cream obiecte din ea, ci doar sa o folosim ca un template pentru clasele copil

In abstractizare exista doua concepte:
- Interfata - contine doar metode abstracte
- Clasa abstracta - contine metode abstracte cat si metode proprii, cu logica
Clasa abstracta trebuie sa mosteneasca clasa ABC (Abstract Class Method)
"""
"""
Polimorfism = poli (mai multe) morfis (forma/forme) => ceva care poate lua mai multe forme
In cazul nostru, in OOP, o metoda poate sa aible acelasi nume in clase diferite dar implementari/logica diferita in interior
ex: nr_roti,nr_locuri
"""


from abc import ABC, abstractmethod

#punem ABC pt a-i zice la Python ca este o cls abstracta
# in java se defineste: class abstract numeClasa
class Vehicul(ABC):
    @abstractmethod # am folosit un decorator sa marcam aceasta metoda ca abstracta
    def nr_locuri(self):
        raise NotImplementedError

# in general, met abs nu trebuie sa aibe o logica proprie
# pt a nu avea erori, avem 2 optiuni:
    #scriem "pass"
    #raise NotImplementedError - ridicam exceptie

    @abstractmethod
    def nr_roti(self):
        pass

# am folosit un decorator ca sa marcam metoda ca fiind una de clasa, cu logica proprie
    @classmethod
    def metoda_logica_proprie(self):
        print(f"Aici este o met cu logica proprie,"
              f"NU trebuie implementata obligatoriu in clasele copil ")

class Masina(Vehicul):
    def __init__(self, culoare):
        self.culoare = culoare

    def get_culoare(self):
        return self.culoare

    def nr_roti(self):
        return 4

    def nr_locuri(self):
        return 2


class Bicicleta(Vehicul):
    def __init__(self, roti_ajutatoare = True):
        self.roti_ajutatoare = roti_ajutatoare

    def nr_roti(self):
        if self.roti_ajutatoare == True:
            return 4
        else:
            return 2
    def nr_locuri(self):
        return 1



# audi = Masina("gri") # nu o sa mearga deoarece nu avem clasele abstracte instantiate in cls copil
# # de aceea, in cls Masina o sa instantiem nr locuri si nr roti
# audi.metoda_logica_proprie()
# print(audi.nr_locuri())
# print(audi.nr_roti())
# print(audi.get_culoare())

# putem crea un obiecvt de tip Persoana?
# vehicul = Vehicul()

### !!!! NU putem crea obiecte din clase abstracte (exemplu vehicul = Vehicul())
## ne folosim de clasele copil ca sa putem crea obiecte,
# deoarece acolo rescriem clasele abstracte

bici = Bicicleta()
print(bici.nr_roti())
