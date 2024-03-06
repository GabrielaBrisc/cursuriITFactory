##### TUPLE #####

"""
Păstrează mai multe valori imbutabile într-o singură variabilă.
● Valorile sunt ordonate, încep de la index 0.
● Valorile sunt imutabile, odată definite, așa rămân. Nu se mai pot adăuga/șterge valori.
● Acceptă valori duplicate.
● Putem folosi len() pentru a afla dimensiunea.
"""

### Crearea unei tuple ###

# tupla = ()
# print(type(tupla))
#SAU
tupla = tuple()
print(tupla)
print(type(tupla))

### ATENTIE!!! ###
nu_este_tupla = ("String")
print(type(nu_este_tupla)) # este de tip string, nu este o tupla
aceasta_Este_o_tupla_cu_un_sg_elem = ("string",)
print(type(aceasta_Este_o_tupla_cu_un_sg_elem))

tupla1 = (1, 2 ,3 ,4 ,5, 1)
# print(tupla1.count(1))
# print(tupla1.index(2)) # returneaza indexul de la valoarea introdusa; indexul de la valoarea 4 este 3
#indexul de la valoarea 2 este 1
print(tupla1[0])
print(tupla1[-2])
print(tupla1[::-1])

### Adaugare element ###

# tupla1[0] = 4 # da eroare

### Mic hack
tupla1 = list(tupla1) #casting la lista
#modificam elementul de pe pozitia 1
tupla1[0] = 4 #modificam elementul de pe pozitia 1
tupla1 += [4] #adaugam element in lista
tupla1 = tuple(tupla1) # transformam din nou in tupla
print(tupla1)

### Unpack
tupla2 = (1,2,3)
x,y,z = tupla2
print(x,y,z)