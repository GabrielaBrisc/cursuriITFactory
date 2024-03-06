##### FOR / FOR ELSE #####

"""
range -> este o functie care defineste un interval
    range(A,B,C)
    A = de unde incepem. Daca nu punem nimic, default este 0, ex: range(4) <=> 0, 1, 2, 3
    B = pana unde mergem. Daca nu punem, atunci va fi limita superioara -1 ex: range(4) <=> 0, 1, 2, 3
    C = pasul - optional (default este 1),
        dar cand punem pasul, trebuie neaparat sa avem si A si B
"""
# Avem doar A si B, pasul e by default
# for i in range(3,12):
#     print(i)

# Avem pasul, e necesar sa avem si A si B
# for i in range(0, 12, 2):
#     print(i)

# for i in range(12, 2, -1):
#     print(i)

# # Avem doar B, adica pana unde mergem
# for i in range (33):
#     print(i)

##### FOR EACH #####
# for i in [1,3,4,6,7, "mere", 9, True]:
#     print(i)
# print("--------------------------")
# ### SAU cu FOR si lista
# lista = [1,3,4,6,7, "mere", 9, True]
# for i in range(len(lista)):
#     print(lista[i])
