"""
 - private -> metoda/atributul nu poate fi accesat decat in interiorul clasei in care este definita
           -> se scrie cu __ la inceputul numelui
De ex:    def __init__(self, var_private):
        self.__variabila_privata = var_private

 - protected -> metoda/atributul poate fi accesat din clasa in care a fost definita
                dar si in clasele copil ale acesteia
                INSA NU DIN EXTERIOR
             -> se defineste cu _ (_exemplu)
"""
class Car:

    # atribute din clasa
    #variabila privata:
    __variabila_privata = "Test1"
    _variabila_protected = "Protected"

#metoda/atribut private accesat in clasa parinte
    # def __init__(self, var_private):
    #     self.__variabila_privata = var_private

    def __init__(self, var_protected):
        self._variabila_protected = var_protected

    def get_var_private(self):
        return self.__variabila_privata

    def set_var_private(self, value):
        self.__variabila_privata = value

    def __hidden_method(self):
        print("Hello, you cannot call me")



car = Car(12)
# print(car._variabila_protected)
print(car.get_var_private())
car.set_var_private("am fost modificat")
print(car.get_var_private())
#nu avem acces la cea hidden: nu o gaseste
# car.__hidden
