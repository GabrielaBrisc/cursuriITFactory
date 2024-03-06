##### DICTIONARE #####
"""
● Dicționarele păstrează date de tip cheie: valoare.
● Dict-urile sunt ordonate.
● Dict-urile sunt mutabile, deci valorile pot fi schimbate.
● Cheile sunt unice, nu putem avea chei duplicate, ar crea confuzie.
● Cheile sunt ca niște porecle pentru index-uri.
● Putem folosi len() pentru a afla dimensiunea.
-> O cheie poate avea o singura valoare, daca ne dorim mai multe, la valoare punem o lista cu valori
eg: "limbi_vorbite": ["Romana", "Eng", "Germana"]

"""

### Crearea unui dict ###
# dictionar_gol = {}
# print(type(dictionar_gol))
# dictionar_gol = dict()
# print(type(dictionar_gol))
# dictionar = {
#             "nume": "Vlad",
#             "varsta": 23,
#             "tara": "Romania",
#             "limbi_vorbite": ["Romana", "Eng", "Germana"]
#             }
# dictionar = dict(nume="Vlad", varsta = 23, tara = "Romania", limbi_vorbite = ["Romana", "Eng", "Germana"])
# print(dictionar)

### Cheile sunt unice (nu accepta duplicate) ###
# dictionar = {
#             "nume": "Vlad",
#             "varsta": 23,
#             "tara": "Romania",
#             "tara": "Germania", # se suprascrie Romania, o sa returneze Germania
#             "limbi_vorbite": ["Romana", "Eng", "Germana"]
#             }
# print(dictionar)


### Accesare elemente ale unui dictionar ->  prin chei
# dictionar = {
#             "nume": "Vlad",
#             "varsta": 23,
#             "tara": "Romania",
#             "limbi_vorbite": ["Romana", "Eng", "Germana"]
#             }
# tara_Vlad = dictionar.get("tara")
# print(tara_Vlad)
#sau:
# tara_Vlad_2 = dictionar["tara"]
# print(tara_Vlad_2)

# Accesarea tuturor valorilor dintr un dictionar
# print(dictionar.values())

# Accesarea tuturor cheilor dintr un dictionar
# print(dictionar.keys())

# Returneaza toti itemii dintr un dictionar
# print(dictionar.items())

### Schimbarea unui element ###
# dictionar["tara"] = "Germania"
# print(dictionar)
# print(dictionar["tara"])
# #SAU:
# dictionar.update({"tara": "Franta"})
# print(dictionar)

### Adaugarea unui element ###
dictionar = {
            "nume": "Vlad",
            "varsta": 23,
            "tara": "Romania",
            "limbi_vorbite": ["Romana", "Eng", "Germana"]
            }
dictionar["Sex"] = "Masculin"
print(dictionar)
dictionar.update({"CNP": "210000"})
print(dictionar)

### Stergerea unui element ###
dictionar.pop("CNP")
print(dictionar)
#SAU
# se merge pe principiul lifo (scoate ultima valoare adaugata din dictionar
dictionar.popitem() # scoate ultima cheie:valoare din dictionar
print(dictionar)

### Stergerea tuturor elementelor din dict ###
dictionar.clear()
print(dictionar)

## Lungimea unui dictionar ###
print(len(dictionar))


