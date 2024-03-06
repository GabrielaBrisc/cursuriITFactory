#####	Exercitii    #####
'''
Simulam functionalitatea unui bancomat.
Verificam username-ul si parola. User-ul are doar 2 incercari pentru introducerea atat a username-ului cat si a parolei.
User-ul poate sa scoata o suma de bani mai mica decat sold-ul curent. Daca introduce o suma prea mare poate
sa aleaga daca doreste sa reincerce sau nu. La a doua incercare, daca user-ul introduce din nou o suma prea mare,
se iese din program.

expected_username = "username"
expected_password = "parola"
sold = 5.00
'''

expected_username = "username"
expected_password = "parola"
sold = 5000
user_name = input("Introduceti username-ul: ")
if user_name == expected_username:
    print("User name corect")
else:
    user_name = input("Reintroduceti username-ul: ")
    assert user_name == expected_username, "Ati introdus un username gresit"
    print("A doua oara User name e corect")

parola = input("Itroduceti parola: ")
if parola == expected_password:
    print("Parola corecta")
else:
    parola = input("Reintroduceti parola: ")
    assert parola == expected_password, "Ati introdus o parola gresita"
    print("Parola introdusa a doua oara e corecta")

sold_de_retras = float(input("Intro suma de retras: "))
if sold_de_retras <= sold:
    print(f"Am scos suma de {sold_de_retras}")
else:
    print("Ati introdus o suma mai mare decat ce aveti in cont.",
          "Doriti sa reincercati?")
    raspuns = input("Tastati da daca doriti sa reincercati: ")
    if raspuns == "da":
        sold_de_retras = float(input("Intro suma de retras: "))
        assert sold_de_retras <= sold, "Fonduri insuficiente!"
        print(f"Ridicati suma {sold_de_retras}")
    elif raspuns == "nu":
        print("O zi frumoassa!")
    else:
        print("Bye!")





