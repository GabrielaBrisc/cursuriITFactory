"""
Exercitiu:
Type a one-letter command and hit enter:
A to add a name to your list
R to remove a name from your list
S to show the names in your list
Q to quit
"""

names = ['Ariana', "Elena"]
ALLOW_COMMANDS = ['a','r', 's', 'q']
continue_loop = True

while continue_loop: # se va iesi din while atunci cand continue_loop = False
    command = input("Introduceti comanda ['A','R', 'S', 'Q']: ").lower()

    if command in ALLOW_COMMANDS:
        if command == 'a':
            name = input("Introduceti un nume pt a-l adauga: ")
            names.append(name) # sau names = names + name
        if command == 'r':
            name = input("Introduceti un nume pt a-l sterge:")
            names.remove(name)
        elif command == 's':
            print(f"Lista actuala este: {names}")
        else:
            break
            #sau:
            # continue_loop = False # aici introducem Q de la tastatura
    else:
        print(f"Introduceti o comanda valida, alegeti intre: ['A','R', 'S', 'Q']")


