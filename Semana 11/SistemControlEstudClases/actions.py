class Student:
    def __init__(self, name, section, spanish, english, social_studies, ciencies, average):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social_studies = social_studies
        self.ciencies = ciencies
        self.average = average

    def convert_to_dic(self):
        dic = {
            "Nombre": self.name,
            "Seccion": self.section,
            "Español": self.spanish,
            "Ingles": self.english,
            "Estudios_Sociales": self.social_studies,
            "Ciencias": self.ciencies,
            "Promedio": self.average
        }
        return dic


def enter_students_info(students_list):
    option = 1
    while option == 1:
        name = input("Ingrese nombre completo: ")
        section = input("Ingrese seccion: ")
        spanish = validate_note("Ingrese nota de Español: ")
        english = validate_note("Ingrese nota de ingles: ")
        social_studies = validate_note("Ingrese nota de Estudios Sociales: ")
        ciencies = validate_note("Ingrese nota de Ciencias: ")
        average = (spanish + english + social_studies + ciencies) / 4

        students_list.append(
            Student(name, section, spanish, english, social_studies, ciencies, average)
        )
        
        
        while True:
            try:
                option = int(input("Desea agregar otro estudiante: 1=si / 2=no: "))
                if option in (1, 2):
                    break
                else:
                    print("Opcion invalida")
            except ValueError as e:
                print(f"Ingrese un valor valido: {e}")


def validate_note(message):
    while True:
        try:
            note = float(input(message))
            if 0 <= note <= 100:
                return note
            else:
                print("Nota invalida")
        except ValueError as e:
            print(f'Ingresar un valor valido: {e}')


def print_students_list(students_list):
    if not students_list:
        print("No hay estudiantes registrados")
        return
    for student in students_list:
        print(f"Nombre: {student.name} | Seccion: {student.section} | Nota de Español: {student.spanish} | Nota de Ingles: {student.english} Nota de Estudios Sociales: {student.social_studies} | Nota de Ciencias: {student.ciencies}")
    return students_list


def print_top3_average(students_list):
    if not students_list:
        print("No hay estudiantes ingresados")
        return
    else:    
        sorted_list = sorted(students_list, key=lambda s: s.average, reverse=True)[:3]
        for i, s in enumerate(sorted_list, start=1):
            print(f"{i}. Nombre: {s.name} - Promedio: {s.average}")


def print_overall_average(students_list):
    if not students_list:
        print("No hay estudiantes registrados")
        return
    else:
        averages = []
        for student in students_list:
            averages.append(student.average)

        overall_average = sum(averages) / len(averages)
        print(f' Promedio general de todos los estudiantes: {overall_average}')