##### WHILE / WHILE ELSE #####
"""
Structuri repetitive = blocuri de cod care se vor executa
in mod repetitiv pana cand o anumita conditie nu mai este
respectata (este falsa)

Iteratie = procesul prin care un bloc de cod este executat
in cadrul structurii repetitive
"""
"""
while = "cat timp" cond e adevarata
      = ne permite exe unui bloc de cod cat timpo cond e adev
-i: Contorul de control al structurii repetitive trebuie declarat in afara structurii repetitive
si modif in interiorul blocului de cod
- !!!Atentie!!! Daca nu modificam valoarea contorului in interiorul
struct repetitive, vom crea un loop/ciclu INFINIT
"""
# i = 0
# while i <= 3:
#     print(f"Valoarea lui i inainte de incrementare e: {i}")
#     i += 1
# print('done')

"""
While-ul de mai sus se itereaza astfel:
i = 0 => i<=3? DA => se exe codul din interiorul ciclului
i = 1 => i<=3? DA => se exe codul din interiorul ciclului
i = 2 => i<=3? DA => se exe codul din interiorul ciclului
i = 3 => i<=3? DA => se exe codul din interiorul ciclului
i = 4 => i<=3? NU => se iese din ciclu
"""

# Exemplu ciclu infinit
# i = 0
# while i <= 3:
#     print(i)
#     i -= 1
# print('done')

# Exemplu cu breack
# i = 0
# while i <= 10:
#     print(f"Valoarea lui i este {i}")
#     if i == 5:
#         break # fara el ne afiseaza toate val de la 0 la 10
#     i += 1
# print("Done")

#sau daca nu vrem sa afisam nimic in if, folosim pass
# while i <= 10:
#     print(f"Valoarea lui i este {i}")
#     if i == 5:
#         pass # pt un if, while for in care nu vrem sa scriem nimic
#     i += 1
# print("Done")

# ca sa scapam de ciclul infinit, putem folosi break
# i = 0
# while i <= 3:
#     print(i)
#     if i == -10:
#         break
#     i -= 1
# print("Done")

# while True:
#     print("INFINITY")

# # nu se exe nimic:
# while None:
#     print("INFINITY")

##### WHILE ELSE #####
"""
Folosim WHILE ELSE (Referinta la exemplul de mai sus
WHILE = tipul structurii repetitive
i<=3: conditia care se evalueaza
else: setul de instructiuni care se va executa 
dupa ce se iese din structura repetitiva
"""
# i = 0
# while i <= 20:
#     print(f'i = {i}')
#     i += 1
# else:
#     print(f"i nu mai este <= 20, este {i}")
# print("Done")

"""
Debugging = Depanare = procesul prin care gasim
          si rezolvam probleme in cod (bugs)
          = punem pauza in cod ca sa vedem cum se parcurge
          codul pas cu pas
"""

### Parcurgerea listelor cu while
lista_fructe = ["mere", "pere", "banane", "struguri"]

i = 0
#cat timp i e mai mic decat lungimea listei
while i <= len(lista_fructe)-1: #ori punem len(lista)-1
# ori nu punem egal deoarece o sa crape (index out of range)
    print(f'fruct = {lista_fructe[i]}')
    i += 1
print("Am iesit din while")
