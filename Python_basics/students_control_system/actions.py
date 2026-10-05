def enter_students_info(students_list):
    option = 1
    while option == 1:
        full_name = input("Ingrese nombre completo: ")
        section = input("Ingrese seccion: ")
        spanish_note = validate_note("Ingrese nota de Español: ")
        english_note = validate_note("Ingrese nota de ingles: ")
        social_studies_note = validate_note("Ingrese nota de Estudios Sociales: ")
        sciences_note = validate_note("Ingrese nota de Ciencias: ")
        average = (spanish_note + english_note + social_studies_note + sciences_note) / 4

        students_dic = {
            'nombre': full_name,
            'seccion': section,
            'nota_español': spanish_note,
            'nota_ingles': english_note,
            'nota_estudios_sociales': social_studies_note,
            'nota_ciencias': sciences_note,
            'promedio': average
        }

        students_list.append(students_dic)
        
        
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
        print(f"Nombre: {student['nombre']} | Seccion: {student['seccion']} | Nota de Español: {student['nota_español']} | Nota de Ingles: {student['nota_ingles']} Nota de Estudios Sociales: {student['nota_estudios_sociales']} | Nota de Ciencias: {student['nota_ciencias']}")
    return students_list


def print_top3_average(students_list):
    if not students_list:
        print("No hay estudiantes ingresados")
        return
    else:    
        sorted_list = sorted(students_list, key=lambda s: s['promedio'], reverse=True)[:3]
        for i, s in enumerate(sorted_list, start=1):
            print(f"{i}. Nombre: {s['nombre']} - Promedio: {s['promedio']}")


def print_overall_average(students_list):
    if not students_list:
        print("No hay estudiantes registrados")
        return
    else:
        averages = []
        for student in students_list:
            averages.append(student['promedio'])

        overall_average = sum(averages) / len(averages)
        print(f' Promedio general de todos los estudiantes: {overall_average}')