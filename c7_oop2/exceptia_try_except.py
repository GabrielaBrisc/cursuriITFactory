# elevi = []
#
# while True:
#     nume_elevi = input("Nume elev: ")
#     elevi.append(nume_elevi)
#     if len(elevi) == 5:
#         break
#
# raise Exception("Puteti adauga maxim 5 de elevi")
"""
Exceptiile = clase speciale Python folosite atunci cand ceva nu merge bine in cod
Folosim try - except pentru a gestiona posibilele exceptii aruncate in
codul nostru PENTRU A NU SE OPRI EXECUTAREA PROGRAMULUI
"""

# lista_nr = [1,2,3,4]
# print(lista_nr[6]) #-> ne va arunca o eroare pt ca in lista nu exista elementul cu indexul 6
# print("sunt aici ")

# lista_nr = [1,2,3,4]
# try:
#     print(lista_nr[6])
# except IndexError as error: # aici prindem eroarea si afisam in consola textul erorii
#     print(error)
#     print("incerc index 2 = ",lista_nr[2])
# # error e mesajul erorii pe care il primim
# print("sunt aici dupa IndexError")

### cand nu stim care este eroarea, stim doar ca poate sa apara
# Exception - prinde orice eroare care ar putea aparea
# try:
#     print(lista_nr[6])
# except Exception as error: # Exception poate prinde orice eroare poate aparea in blocul de try:
#     print(error)
# print("sunt aici dupa Exception")

# Exemplu de eroare care nu este prinsa corect
# lista_nr = [1,2,3,4]
#
# try:
#     print(lista_nr[6])
# except AssertionError as error: #AssertionError nu prinde aceeasu eroare ca IndexError
#     #(Generalizat, adica fiecare exceptie prinde doar un anumit tip de eroare
#     # mai putin Exception care prinde orice eroare poate aparea
#     print(error)

# assert 9<8,"9 nu este mai mic ca 8"
# print("sunt aici dupa assert")
#fara try nu o sa mai ajunga la print

#folosim try except pt a se executa codul de dupa assert:
try:
    assert 9 < 8, "9 nu este mai mic ca 8"
except AssertionError as error:
    # pass -> cand nu vrem sa scriem nimic
    print(error)
print("sunt aici dupa try and except assertionError ")

