#Calculeaza primele numere pare pana la 101
# suma = 0
# for i in range(0,102,2):
#     print(i) # verificam ce nr ne da
#     suma += i
# print(suma)

#------ Inverseaza textul folosind for -------
# text = "Ana are mere"
# text_inversat = ""
# print(len(text))
# for i in range(len(text)-1,-1,-1): #echiv cu range(11, -1, -1) deoarece len(text) = 12
#     text_inversat += text[i]
# else:
#     print("S-a terminat range-ul")
# print(text_inversat)

### Exercitiu:
"""
avem o lista de culori: ["roz","albastru","rosu","alb","galben"]
Parcurg lista iar cand ajung la valoarea culoarea alb dau skip
"""
# lista_culori = ["roz","albastru","rosu","alb","galben"]
#
# for culoare in (lista_culori):
#     if culoare == "alb":
#         continue
#     print(culoare)

"""
Avem lista de mai sus. Stergem din lista toate nonculorile (alb, gri, negru)
"""
# lista_culori = ["roz","albastru","negru","rosu","alb","galben"]
#
# for culoare in (lista_culori):
#     if culoare == "alb" or culoare == "negru" or culoare == "gri":
#         lista_culori.remove(culoare)
#         print(f"{culoare} este nonculoare")
# print(lista_culori)

#### Alt exercitiu cu dict
# Cum interam cheie valoare intr-un dictionar?

# note_elevi={
#         "Andrei":10,
#         "Elena": 8,
#         "Maria": 10,
# }
# print(note_elevi.items()) # lista cu tuple cheie:valoare
# for elev, nota in note_elevi.items(): #elev ia valoarea cheii, nota ia valoarea valorii cheii
#     print(f"{elev} a luat nota {nota}")

### Cum iteram printr-un dicionar in dictionar in dictionar etc...
dict1 = {
    "HR":{   #HR e cheia
        "1":{  #la cheia HR se afla acest dict cu cheia "1"
            "Andrei":4532, # in dict i acem
            "Matei":2364,
            "Florin":12353
        },
        "2":{  #dict 2 din dict 1
            "Iulia":56435,
            "Georgiana":1235323,
            "Luca":1634523,
            "Andrei":653224
        }
    }
}
### hr este cheie pt val "1" si "2"
### pt cheia "1" avem valoarea: "Andrei":4532
                             # "Matei":2364,
                             # "Florin":12353

print(dict1.items()) # ne returneaza o tupla

# parcurgem
for cheie, valoare in dict1.items():
    # print(cheie, valoare)
    for cheie_din_hr, valori_din_hr in valoare.items(): ## valoarea noastra e tot un dictionar
        print(cheie_din_hr)
        # print(valori_din_hr)
        # print(cheie_din_hr,valori_din_hr)
        for chei_din_1_2, valori_din_1_2 in valori_din_hr.items():
            print(valori_din_1_2)
            print(chei_din_1_2)



