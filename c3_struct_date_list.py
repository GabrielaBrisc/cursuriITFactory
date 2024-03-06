### STRUCTURI DE DATE ###

##### LISTE #####
"""
 -> Listele sunt structuri de date built-in Python
 -> SUnt folosite pt a stoca mai multe elemen intr-o singura variabila
 -> Crearea unei liste se face cu [] sau list()
"""
"""
    Caracteristicile unei liste
    -> Ordonate
    -> Mutabile -> se pot ADAUGA, STERGE si SCHIMBA elemente in lista
    -> Accepta duplicate
    -> Itemii/elementele listei sunt indexati (primul index este [0])
"""

### CREAREA UNEI LISTE ###
# lista_goala = [] # cea mai uzuala varianta
# print(type(lista_goala))
#
# lista_goala = list() # -> tot o lista goala
# print(type(lista_goala))

# lista = ["masina", 42, True, [1,2,3,4]]
# print(lista)

### Listele sunt ordonate
"""
-> Inseamna ca elem unei liste au o anumita ordine care 
nu se schimba
 Daca adaugam un elem nou, acesta va fi pus la finalul listei
!!! Atentie, exista anumite metode in liste care pot schimba ordinea 
elementelor din lista
"""

# masini = ["Audi", "Volswagen", "BMW", "Volvo","Mercedes"]
# print(masini)

# Accesare elemente
# print("masini[0]= ",masini[0])
# print("masini[-1]=",masini[-1]) # ultimul element; mai poate fi accesat si cu len sa vedem lungimea
# print("masini[:4]", masini[:4])
# print("masini[::-1]", masini[::-1])
# print("masini[2:5]", masini[2:5])
# print("masini[6]", masini[6]) # arunca o exceptie deoarece nu avem acel element

# MUTABILE
# Adaugarea de elemente:

# masini = ["Audi", "Volswagen", "BMW", "Volvo","Mercedes"]
#adaugare prin suprascriere
# masini = masini + ["Toyota"] # ca si element adaugat in lista noastra
# print(masini)
# masini = masini + ["Dacia", "Reno"]
# print(masini)

# append - adaugam ca si lista in lista, nu ca si element in lista
# masini.append(["Toyota"]) # ca si lista, nu ca si element in lista initiala
# print(masini)
# masini.append(["Dacia", "Reno"])
# print(masini)
# print(masini[-1]) # ultimul element este o lista

# adaugam o lista de elemente la lista noastra.
# adica, ca si elemente, nu ca si lista in lista
# masini.extend(["Dacia", "Reno"])
# print(masini)
# ['Audi', 'Volswagen', 'BMW', 'Volvo', 'Mercedes', 'Toyota', 'Dacia', 'Reno', ['Toyota'], ['Dacia', 'Reno'], 'Dacia', 'Reno']
# print(masini[-1])

### Modificare ordine elemente din lista ###
# insert asteapta un index si un obiect,
# =adica inseram pe pozitia pe care ne-o dorim
# masini = ["Audi", "Volswagen", "BMW", "Volvo","Mercedes"]
# masini.insert(1, "Reno") # adauga elem pe pozitia 1,
# # iar pe restul elementelorle muta cu o pozitie la dreapta
#
# masini.insert(len(masini), "Mazda") # adauga pe ultima pozitie
# print(masini)

### Stergerea unui element ###
# masini = ["Audi", "Volswagen", "BMW", "Volvo","Mercedes", "BMW"]
# masini.remove("BMW") # sterge primul element care este egal cu valoareaintrodusa
# print(masini)

# pop = suporta un index (introducem un index, nu valoarea)
# daca nu introducem indexul dorit, va sterge ultimul element si il va returna
# diferenta dintre pop si remove e ca, pop o sa ne si returneze valoarea stearsa
# masina_stearsa = masini.pop()
# print(masina_stearsa)
# print(masini)
# masina_stearsa = masini.remove("Audi") # o sa ne returneze none
# print(masina_stearsa)
# masini.pop(0) # stergem primul element din lista cu ajutorul indexului
# print(masini)

# # stergem toata lista
# masini.clear()
# print(masini)

### Schimbare de elemente ###
masini = ["Audi", "Volswagen", "BMW", "Volvo","Mercedes", "BMW"]
masini[0] = "Dacia"
print(masini)

### Listele accepta duplicate ###
masini = ["Audi", "Volswagen", "BMW","Audi", "Volvo","Mercedes", "Audi", "BMW"]
print(masini)

### Lungimea unei liste ###
print(len(masini))