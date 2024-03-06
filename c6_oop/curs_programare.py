class CursProgramare:

    def __init__(self, companie, nume, durata_curs, nr_locuri):
        #cream fieldurile, atributele:
        self.companie = companie
        self.nume = nume
        self.durata_curs = durata_curs
        self.nr_locuri = nr_locuri
        self.studenti = [] #initial nu avem studenti inscrisi

    def inscriere_student(self, student):
        if self.get_nr_locuri_disponibile() > 0:
            #adaugam noul student in lista noastra
            self.studenti.append(student)
        else:
            print("Nu mai sunt locuri disponibile")

    def descriere_curs(self):
        print(f"{self.companie} - {self.nume} - {self.durata_curs} zile")
        print("-" *30)
        if len(self.studenti) > 0:
            # dorim sa afisam studentii:
            for student in self.studenti:
                print(f"{student.nume} {student.prenume}")
        else:
            print(f"nu sunt studenti inscrisi")

    #vrem sa vedem cate locuri mai sunt, deoarece noi tot aducem studenti
    #iar noi avem o limita de locuri
    def get_nr_locuri_disponibile(self):
        return self.nr_locuri - len(self.studenti)