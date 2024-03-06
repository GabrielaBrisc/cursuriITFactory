from mostenirea import Persoana, Student, Angajat, Profesor

# student1 = Persoana("Adelina", 28, "Constanta")
# student1.descriere()
#
# stud2 = Student("Maria", 21, "Zalau", "ETTI", 2)
# stud2.descriere()
# print(stud2.anul_nasterii())
# print(stud2.nume)
# print(stud2.varsta)

# paul = Angajat("Paul",26,"Simleu", "ITFactory", 5000)
# paul.descriere()
# print(f"Salariul anual: {paul.salariu_anual()}")

elena = Profesor("Elena", 56, "Iasi", "Itfactory", 8000, "Matematica", 21)
elena.descriere()
print("Salariu anual " + str(elena.salariu_anual()))
print("Anul nasterii " + str(elena.anul_nasterii()))