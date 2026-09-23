import csv
import os
from actions import Student


def write_csv_file(file_path, student_list):

    if not student_list:
        print("No hay estudiantes ingresados")
        return
    
    rows = []
    for s in student_list:
        rows.append(s.convert_to_dic())
    headers = rows[0].keys()

    with open(file_path, 'w', encoding='utf-8', newline = '') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Se exportaron {len(student_list)} estudiantes a {file_path}")


def read_csv_file(file_path, student_list):
    if not os.path.exists(file_path):
        print("No hay estudiantes guardados para importar")
        return
    
    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            s = Student(
                name=row['Nombre'],
                section=row['Seccion'],
                spanish=float(row['Español']),
                english=float(row['Ingles']),
                social_studies=float(row['Estudios_Sociales']),
                ciencies=float(row['Ciencias']),
                average=float(row['Promedio'])
            )
            student_list.append(s)
        print(f"Se importaron {len(student_list)} estudiantes previamente guardados en {file_path}")