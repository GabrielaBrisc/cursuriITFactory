# tema 5, ex 3 de la cele optionale, cu dict si lista de frecventa
# avem o lista cu nr de la 0-9

### lista frecventa
#indexul valorilor din lista   0  1  2  3  4  5  6  7  8  9
#valoare frecventa numar       0  2  0  1  0  3  0  2  0  1
#lista                        [1, 3, 1, 5, 9, 7, 7, 5, 5]
def frecventa_cifre(lista):
    #la inceput nu stim care e frecventa cifrelor din Lista, de aceea, lista_frecv e cu 0
    lista_frecventa = [0,0,0,0,0,0,0,0,0,0]
    #cu ajutorul lui numar, parcurgem lista
    for numar in lista:
        #numar o sa fie valoarea din lista =[1, 3, 1, 5, 9, 7, 7, 5, 5]'
        #ne folosim de numar ca si index ca sa punem in lista_frecventa pe pozitia respectiva:exemplu
        # cu ajutorul indexului (numar) ne plimbam prin lista
        #exemplu: lista_frecventa[2] += 1 <=> la indexul 2, valoarea frecventei numarului este 0
        # de aceea lista frecventa o sa fie [0, 2, 0,1,0,3,0,2,0,1] la final
        #cand numar se repeta, se incrementeaza valoarea din lista frecventa, pentru acel numar
        # de ex, cand o sa fim la indexul 2 (valoarea e 1) din lista,
        #in lista frecv, se incrementeaza cu 1 deoarece lista_frecv[1] +=1 o sa fie 2
        # adica 1 apare pt a 2 a oara in lista
        lista_frecventa[numar] +=1
    dictionar_de_frecventa = {}

    # ne construim dictionarul
    for i in range(len(lista_frecventa)):
        dictionar_de_frecventa.update({i:lista_frecventa[i]})
    return dictionar_de_frecventa

rezultat = frecventa_cifre([1, 3, 1, 5, 9, 7, 7, 5, 5])

for key, value in rezultat.items():
    print(f"{key}:{value}")

