##### FUNCTII #####

#definirea functiei (fara parametrii si return)
def say_hello():
    print("Hello, Gabi!")

#apelam functia
# say_hello()

# !!! Daca o functie nu este apelata, codul din interiorul ei nu va fi executat
#  De aceea se spune ca functiile ruleaza independent, sunt niste programe in miniatura

# functia say_hello() nu returneaza nimic:
#print(say_hello()) # ne returneaza atat ce e in interiorul functiei cat si None
# noi am apelat functia cu print(Say_hello()), dar print ul returneaza None

# x = say_hello() #apelam functia, ne returneaza Hello, Gabi
# print("x=", x) # ne returneaza none, deoarece functia noastra returneaza none
# # nu avem return si de aia avem none?


#apelam o functie din alt fisier in care a fost creata

from c5_utils_file import say_hi_name
# Apelare functie cu parametru
# Gabi este argumentul parametrului name
say_hi_name("Gabi")
# say_hi_name() # arunca o eroare
