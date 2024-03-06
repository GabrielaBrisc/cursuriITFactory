##### Set-uri #####


### Declarare/ creare set ###
# set_gol = set()
# print(type(set_gol))

# set_gol = {}
# print(type(set_gol)) # --> Atentie, se creaza dictionar

# fructe = {"mere"}
# print(type(fructe))

### Caracteristici ale set-ului ###
"""
● Nu accepta duplicate, Set-urile păstrează mai multe valori unice într-o variabilă.
● Nu sunt ordonate sau indexate.
● Datorită acestui fapt sunt și imutabile (nu putem schimba locația elementelor).
● Imutabile -> Se pot doar adăuga sau șterge elemente.
● Putem folosi len() pentru a afla dimensiunea.
"""

# fructe = {"mere", "pere", "cirese", "caise"}
# print(fructe)

### Nu accepta duplicate ###
# fructe = {"mere", "cirese", "pere", "cirese", "caise", "pere"}
# print(fructe)

### Adaugarea unui element ###
# fructe.add("portocale")
# print(fructe)
# putem pune valori de diferite tipuri
# fructe.add(15)
# print(fructe)

### Adaugarea unui set in alt set ###
# fructe2 = {"ananas", "banane", "pepene"}
# fructe.update(fructe2) # modificam set-ul fruncte, fructe2 ramane neschimbat
# print(fructe)
# print(fructe2)

### Adaugarea unei liste intr un set ###
# fructe_lista = ["ananas", "banane", "pepene"] # ATENTIE: nu accepta doar set-uri, putem intro si liste sau tuple
# fructe.update(fructe_lista)
# print(fructe)

### Stergerea unui element din set ###
# fructe = {"mere", "pere", "cirese", "caise"}
#
# fructe.remove("caise")
# print(fructe)
# fructe.remove("ananas") # o sa ne dea eroare ca nu il avem in lista
# print(fructe)

# fructe.discard("ananas") # aceasta metoda nu o sa dea eroare
# print(fructe)

### Stergerea set-ului ###
# fructe.clear()
# print(fructe)

### Adaugarea unei tuple intr un set ###
