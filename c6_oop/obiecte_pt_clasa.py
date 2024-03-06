# from masina import Masina
#
# #aceste linii functioneaza atat timp cat noi nu avem constructorul
# # audi = Masina()
# # #am aces la toate atributele
# # print(audi.model)
# # print(audi.marca)
# # print(audi.culoare)
# # print(audi.motor_pornit)
# # audi.marca = "Audi"
# # print(audi.marca)
#
# #dupa definirea constructorului avem:
#
# audi = Masina("Audi", "A5")
# # print(audi.marca)
# # print(audi.model)
#
# #se poate si sa scriem atributele
# bmw = Masina(model="X5", marca = "BMW")
# # print(bmw.marca)
# # print(bmw.model)
# # print(bmw.viteza)
#
# # dupa crearea metodei prezentare_masina:
# audi.prezentare_masina()
# bmw.culoare = "negru"
# bmw.prezentare_masina()
#
# #dupa crearea metodelor start, stop, accelereaza:
# audi.start()
# audi.accelereaza(20)
# audi.prezentare_masina()
# audi.accelereaza(40)
# audi.prezentare_masina()
# audi.incetineste(30)
# print(audi.motor_pornit)
# audi.stop()
# print(audi.viteza)
# print(audi.motor_pornit)

### Obiecte din clasa masina si ob din cls persoana
### cream obiecte pentru clasa persoana

from persoana import Persoana
from curs_programare import CursProgramare

curs_TA = CursProgramare("IT Factory", "TA", 15, 12)
curs_TA.descriere_curs()

#inscriem studenti:
student1 = Persoana("Brisc", "Gabriela", 28)
student2 = Persoana("Pop", "Elena", 28)
student3 = Persoana("Pop", "Elena", 28)
student4 = Persoana("Pop", "Elena", 28)
student5 = Persoana("Pop", "Elena", 28)
student6 = Persoana("Pop", "Elena", 28)
student7 = Persoana("Pop", "Elena", 28)
student8 = Persoana("Pop", "Elena", 28)
student9 = Persoana("Pop", "Elena", 28)
student10 = Persoana("Pop", "Elena", 28)
student11 = Persoana("Pop", "Elena", 28)
student12 = Persoana("Pop", "Elena", 28)
student13 = Persoana("Pop", "Elena", 28)
student14 = Persoana("Pop", "Elena", 28)

curs_TA.inscriere_student(student1)
curs_TA.inscriere_student(student2)
curs_TA.inscriere_student(student3)
curs_TA.inscriere_student(student4)
curs_TA.inscriere_student(student5)
curs_TA.inscriere_student(student6)
curs_TA.inscriere_student(student7)
curs_TA.inscriere_student(student8)
curs_TA.inscriere_student(student9)
curs_TA.inscriere_student(student10)
curs_TA.inscriere_student(student11)
curs_TA.inscriere_student(student12)
curs_TA.inscriere_student(student13)
curs_TA.inscriere_student(student14)
curs_TA.descriere_curs()

# alt obiect
curs_TA2 = CursProgramare("IT Factory", "TA", 15, 12)
curs_TA2.descriere_curs()