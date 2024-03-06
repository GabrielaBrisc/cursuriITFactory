"""
FizzBuzz
Introduceti o valoare de la tastatura.
Daca aceasta valoare este multiplu de 3 afisati "Fizz" in loc de numar.
Daca numarul este multiplu de 5 afisati "Buzz" in loc de numar.
Pentru numerele care sunt multiplu si de 5 si de 3 afisati "FizzBuzz"
"""

valoare = int(input("Introduceti valoarea: "))
if valoare %3 == 0 and valoare % 5 == 0:
    print('FizzBuzz')
elif valoare % 3 == 0:
    print('Fizz')
elif valoare % 5 == 0:
    print('Buzz')
else:
    print(valoare, "Salut")