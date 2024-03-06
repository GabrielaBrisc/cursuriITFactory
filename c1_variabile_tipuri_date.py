# print("Hello World")

#comentarii = linii din codul sursa care nu sunt extecutate (menite pentru adnotari/explicatii)
# comentariu pe o sg linie
# pentru comentarii pe mai multe linii folosim: """ """ sau ''' '''

"""
  Zona de comentariu extinsa fol ghilimele
  x= 5
  y= 10
"""

'''
   Zona de comentariu extinsa fol ghilimele
  x= 5
  y= 10
  print("Al doilea hello"
'''

#variabile

"""
1. O variabila este o zona de memorie rezervata in sistem care poate stoca info
2. Poate fi modificata 
3. Variabila este creata doar dupa ce i se asigneaza o valoare
eg: variabila = 5
4. Reguli de denumire a unei variabile: 
    - nu pot contine spatii
    - nu pot sa fie denumite cu nume rezervat (nu putem avea o variabila numita print)
    - trebuie sa fie unice
    - nu pot incepe cu un nr, dar pot contine un nr in numele lor de eg: var5
    - denumirea este case seinsitive (o var numita camelCase nu e aceeasi cu camelcase)
5. Conventii in Python:
    - pt nume de clase: pascalCase
    - pt nume de var/metode: snake_case
    - pt constante: NUME_CONSTANTA
Constantele sunt spatii de memorie care nu isi schimba valoarea
!!! In Python exista DOAR ca si concept ideea de constanta
"""

# Declarare si initializare de variabile
# model_masina = "V60"
# model_Masina = "V10"
# print(model_masina)
# print(model_Masina)
#
# # Constante
# NUME_MASINA = "Dacia"
# print(NUME_MASINA)
# NUME_MASINA = "Audi"
# print(NUME_MASINA)

# Modificarea tipului de date
# model_masina = "V10"
# print(type(model_masina))
# model_masina = 330
# print(type(model_masina))
# model_masina = "310"
# print("1. ",type(model_masina))
# model_masina = int ("310")
# print("2. ",type(model_masina))
#
# print("a+b ca string =", "a"+"b") # concatenare
# print("3+3 ca int =", 3 + 3)
# print("3+3 ca string =", "3"+"3") # concatenare

#cast = trecerea de la un tip la altul
# de la int la string se poate face, invers nu:
# v = str(3)
# print("Cast de la int la string: ", type(v))
# v = str(3+3)
# print("str 3+3: ",v)
# v = str("3"+"3")
# print(v)

# b = int("a") -> nu se poate face cast la int
# print(b)

# x, y, z = "Luni", "Marti", 3
# print(x,y,z)
# x = y = z = "sambata"
# print(x,y,z)

# ------------------------------------------------

### TIPURI DE DATE ###
"""
1. Un tip de date este o info care ii spune sistemului ce tip de info putem stoca intr-o variabila

Cele mai folosite tipuri de date:
    - int (intreg) -> Poate stoca doar valori intregi (fara virgula)
    - float -> poate stoca valori cu zecimale (16 -> 16.0)
    - bool -> True/False
    - string -> poate stoca text (sir de caractere)
"""

# a = 3        #int
# b = 5.5      #float
# c = False    #bool
# d = "String" #string
#
# print(type(a), type(b), type(c), type(d))

#-----------------------------------------------------
### FUNCTIA PRINT ###
"""
print() = o functie Python care ne ajuta sa afisam ce ii dam intre paranteze in consola
"""
# print("Hello World")
#
# nume = "Vlad"
# varsta = 22
# # print("Ma numesc" + nume + "si am varsta de: " + varsta) # ne da eroare deoarece varsta e int
# print("Ma numesc" + nume + "si am varsta de: " + str(varsta))
# print(f"Ma numesc {nume} si am varsta de {varsta}") # Varianta recomandata

#-----------------------------------------------------
### FUNCTIA INPUT ###
#introducem din consola

# nume = input("Introduceti nume: ") # introducem numele de la consola
# print(nume) #vedem ce e salvat in acea variabila
# varsta = input("Introduceti varsta: ")
# print(varsta)
# print(type(varsta)) # e de tip str
# varsta = int(input("Introduceti varsta: "))
# print(varsta)
# print(type(varsta))

#--------------------------------------------------------
### ASSERT ###

# a = 1
# assert  a== 1
# print("A este egal cu 1")
# assert a == 2, "A nu este egal cu 2, nu o sa se mai execute restul liniilor de cod"
# print("Nu mai ajungem aici la rularea programului")

# user_password = input("Password: ")
# expected_pass = "parola123"
# assert user_password == expected_pass, "Parola incorecta"
# print("Correct password")

#--------------------------------------------------------------------
### STRING ###
"""
- fiecare caracter are un index (primul caracter are index 0)
- putem sa taiem (slice) un string fol urmatoarea sintaxa:
        my_str[start_pos:end_pos:step]
-step e pasul, din cat in cat taiem
"""

example = "Februarie"
print(len(example))
print(example[0])
print(example[1])
print(example[2:5])
print(example[-1])
print(example[-3:-1])
print(example[::-1])
print(example[2::2])

# index:   0  1  2  3  4  5  6  7  8
#caracter: F  E  B  R  U  A  R  I  E
#negative:-9 -8 -7 -6 -5 -4 -3 -2 -1

# print(example.count("e"))
# print(example.replace("e", "7"))
# print(example.upper())

new_example = example.replace("e","7")
print(new_example)

# () -> sunt folosite cand apelam functii
# [] -> folosite pt liste, slice
# {} -> dictionare/set-uri

