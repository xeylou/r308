#!/usr/bin/env python3

'''
gestion d'étudiants, de leurs notes & des promotions avec des objets simples

liste des étudiants (tableau de dictionnaires): identifiant, nom, prénom
notes (tableau de tableaux): identifiant étudiant, note, coefficient
promotion (tableau de tableaux): nom, identifiant des étudiants
'''

def insert_grade(input_student:str)->list:
    input_grade=input(f"What is {input_student} grade? ")
    input_coef=input(f"What is the coefficient? ")
    for student_info in student_list:
        if student_info.get("name")==input_student:
            student_id=student_info.get("id")
    grades_list.append([student_id, input_grade, input_coef])
    return(grades_list)

def student_grades(input_student:str)->list:
    for student_info in student_list:
        if student_info.get("name")==input_student:
            student_id=student_info.get("id")
    student_grades=[]
    for grades in grades_list:
        if grades[0]==student_id:
            student_grades.append([grades[1],grades[2]])
    return(student_grades)

def get_average(input_student:str)->float:
    grades=student_grades(input_student)
    average=0
    for grade in grades:
        average+=grade[0]*grade[1]
    return(average/len(grades))

def insert_student(input_student:str)->list:
    input_prom=input(f"prom name: ")
    for student_info in student_list:
        if student_info.get("name")==input_student:
            student_id=student_info.get("id")
    for prom in proms_list:
        if prom[0]==input_prom:
            if student_id not in prom[1]:
                prom[1].append(student_id)
    return(proms_list)

def prom_students(input_prom:str)->int:
    for prom in proms_list:
        if prom[0]==input_prom:
            return(len(prom[1]))

def prom_average(input_prom:str)->float:
    for prom in proms_list:
        if prom[0]==input_prom:
            for student_id in prom[1]:
                for student_info in student_list:
                    if student_info.get("id")==student_id:
                        student_name=student_info.get("name")
                total_average=0
                if (get_average(student_name)==0):
                    pass
                total_average+=get_average(student_name)
            return(total_average/len(prom[1]))


# init testing

student_1 = {"id": 1, "name": "nom1", "surname": "prenom1"}
student_2 = {"id": 2, "name": "nom2", "surname": "prenom2"}

student_list = [student_1, student_2]

grades_list = [[1, 10, 1], [1, 5, 2], [2, 20, 1]]

proms_list = [["prom1", [1, 2]]]

# debugging

# print(insert_grade("nom1"))
# print(student_grades("nom2"))
# print(get_average("nom1"))
# print(insert_student("nom2"))
# print(prom_students("prom1"))
# print(prom_average("prom1"))