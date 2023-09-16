'''
gestion d'étudiants, de leurs notes & des promotions orienté objet
'''

class Etudiant:

    def __init__(self, identifier, name, surname, grades = []):
        self.id = identifier
        self.name = name
        self.surname = surname
        self.grades = grades
    
    def addGrade(self, grade, coeff):
        self.grades.append([grade, coeff])
        return(self.grades)
    
    def gradesNumber(self):
        return(len(self.grades))
    
    def average(self):
        average=0
        for grade in self.grades:
            average+=grade[0]*grade[1]
        return(average/len(self.grades))
    
    def info(self):
        return(f"\nid: {self.id}\nname: {self.name}\nsurname: {self.surname}\ngrades: {self.grades}\n")

# testing objects

student_1 = Etudiant(1, "nom1", "prenom1", [[10, 1]])
student_2 = Etudiant(2, "nom2", "prenom2", [[5, 1]])

# debugging (uncomment to test a method)

# print(student_1.addGrade(1, 1))
# print(student_1.gradesNumber())
# print(student_1.average())
# print(student_1.info())


class Prom:

    def __init__(self, name, student_list = []):
        self.name = name
        self.student_list = student_list
    
    def addStudent(self, input_student: Etudiant):
        if isinstance(input_student, Etudiant):
            self.student_list.append(input_student)
    
    def studentNumber(self):
        return(len(self.student_list))
    
    def average(self):
        prom_average=0
        for student in self.student_list:
            if student.average()==0:
                pass
            prom_average+=student.average()
        return(prom_average/len(self.student_list))

# testing object

prom1 = Prom("prom1", [student_1, student_2])

# debugging

# print(prom1.addStudent(student_1))
# print(prom1.studentNumber())
# print(prom1.average())