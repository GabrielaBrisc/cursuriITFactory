#####	Flow Control   #####
### If ###
""""
● În engleză acest principiu se numește ‘flow control’ - controlăm pe unde curge codul
● Un if simplu e ca o ușă: daca ușa e deschisă (true), se va executa codul din spate. Dacă ușa
(condiția) e închisă (false), python nu va afla ce e în spatele ușii. Pentru Python, acea zona
de cod e inaccesibilă, nu există.
● După cele: ale unei ramuri, când apăsăm ‘Enter’ se vor pune automat 4 spații sau un TAB
Acest lucru se numește indentare. Indentarea are scopul de a-i transmite lui python de unde până
unde ține blocul de cod corespunzător acelei condiții. Sau, altfel spus, marchează pereții camerei
din spatele ușii.
"""
# print("*"*5,"Flow Control","*"*5)
# print("*"*3,"If simplu","*"*3)
#
# nota_de_trecere = 4.5
# nota = float(input("introduce-ti nota: "))
# nota = 5
# if nota > nota_de_trecere:
#     print(f"Felicitari, ai luat nota {nota}")
# print("Am trecut de if-ul de mai sus")

# cu metoda if else
# print("*"*3,"If else","*"*3)
# nota = float(input("introduce-ti nota: "))
# if nota > nota_de_trecere:
#     print(f"Felicitari, ai luat nota {nota}")
# else:
#     print(f"ne pare rau dar ai picat exam cu nota 1 {nota}")

#-------------------------------------------------
### if... else if... else ###

"""
● Se folosește când avem mai mult de 2 situații posibile.
● Condițiile se evaluează de sus în jos.
● Se execută codul aferent primei condiții adevărate.
● După ce s-a găsit cu true, nu se mai verifică ce a mai rămas mai jos.
● Un singur if la început.
● Oricâte elif-uri sunt necesare.
● Un singur else la final.
● Dacă nu găsește niciun true mai sus,
else se vă executa automat (e ca un default).
"""
print("*"*3,"If.. elif.. else","*"*3)
optiune = int(input("Alege o optiune [0, 1, 2]: "))

if optiune == 0:
    print("ai ales 0")
elif optiune == 1:
    print("ai ales 1")
elif optiune == 2:
    print("ai ales 2")
else:
    print("Nu ai ales nicio optiune valida")

