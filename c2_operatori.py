#####   Operatori de atribuire    ####
"""
Atribuire/Asignare = proces prin care salvam informatii la adresa de
memorie identificata cu un nume al variabilei
"""
"""
 = --> x=5
+= --> x += 1 <=> x = x+1
-= --> x -= 1 <=> x = x-1
*= --> x *= 3 <=> x = x*3
/= --> x /= 3 <=> x = x/3

"""
print("*"*5,"Operatori de atribuire","*"*5)
x = 5
print("x =", x)
x += 3
print("x += 3:", x)
x -= 4
print("x -= 4:", x)
x *= 10
print("x *= 10:", x)
x /= 10
print("x /= 10:", x)

#----------------------------------------------------
#####   Operatori aritmetici    ####

"""
+ adunare ->> x+y
- scadare ->> x-y
* inmultire ->> x*y
/ impartire ->> x/y
// Floor division ->> x//y (rotunjeste rezultatul la cel mai apropiat nr intreg inferior
 %   Modulo         --> x%y (Returneaza Restul impartirii)
**  Exponential    --> x**y
"""
print("*"*5,"Operatori aritmetici","*"*5)
x = 7
y = 3
print("x+y=",x+y)
print("x-y=",x-y)
print("x*y=",x*y)
print("x/y=",x/y)
print("x//y=",x//y)
print("x%y=",x%y) # restul impartirii
print("x**y=",x**y)

# ------------------------------------------------------------------------------------- #

#####	Operatori Logici    #####

"""
and --> Returneaza True daca ambele conditii sunt adevarate --> x > 5 and x < 10
or  --> Returneaza True daca cel putin o conditie este adevarata --> x > 5 or x == 2
not --> Retunreaza True daca rezultatul conditiei este Fals si vice-versa --> not(x<5), not(x > 5 and x < 10)
Oridinea prioritatii NOT > AND > OR
"""

print("*"*5,"Operatori logici","*"*5)
x = 2
print("and-->",x > 5 and x < 10)
print("or-->",x > 5 or x == 2)
print("not-->",not(x > 5 and x < 10))

#NOT > AND >OR
print(not( x> 5) or x < 10 and x == 3) #not(False) or True and False --> True or True and False (prima data face true and false) -> True
print (not x < 5)
# ------------------------------------------------------------------------------------- #

#####	Operatori de comparare    #####
"""
==  --> Equal                       --> x == y (Verifica daca x este egal cu y) 
!=  --> Not Equal                   --> x != y (Verifica daca x este diferit cu y)
>   --> Greater then                --> x > y  (Verifica daca x este mai mare y)
<   --> Less then                   --> x < y  (Verifica daca x este mai mic decat y)
>=  --> Greater then or equal to    --> x >= y
<=  --> Less then or equal to       --> x <= y
Oridinea prioritatii NOT > AND > OR
"""
print("*"*5,"Operatori de comparare","*"*5)
x = 2
y = 10
print(f"{x}=={y} -->",x == y)
print(f"{x}!={y} ->>", x!=y)
print(f"{x}>{y} ->>", x>y)
print(f"{x}<{y}-->", x<y)
print(f"{x}>={y}-->", x>=y)
print(f"{x}<={y}-->", x<=y)
print("-"*10)
x = 12
y = 12
print(f"{x}>{y} ->>", x>y)
print(f"{x}<{y}-->", x<y)
print(f"{x}>={y}-->", x>=y)
print(f"{x}<={y}-->", x<=y)

a = 10
b = 20
c = 30
#       F    or  F   and    T   => F
print( a > b or b > c and c == 30 )   # inseamna  a > b or ( b > c and c == 30 )
#       F    and   F   or  F     and    T
#             F        or         F      => F
print( a > b and b > c or a == 15 and c == 30 )   # inseamna (a > b and b > c) or (a == 15 and c == 30)
#     not   F    and   F    or    T
#       T       and    F    or     T
#                F          or     T     => T
print( not a > b and a == 15 or c == 30 )  # inseamna ((not a > b) and a == 15) or c == 30

# ------------------------------------------------------------------------------------- #