import csv
import os


def write_csv_file(file_path, student_list, headers):
    if not student_list:
        print("No hay estudiantes ingresados")
        return
    
    with open(file_path, 'w', encoding='utf-8', newline = '') as file:
        writer = csv.DictWriter(file, headers,)
        writer.writeheader()
        writer.writerows(student_list)
    print(f"Se exportaron {len(student_list)} estudiantes a {file_path}")


def read_csv_file(file_path, student_list):
    if not os.path.exists(file_path):
        print("No hay estudiantes guardados para importar")
        return
    
    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for i in ('nota_español', 'nota_ingles', 'nota_estudios_sociales', 'nota_ciencias', 'promedio'):
                row[i] = float(row[i])
            student_list.append(row)
        print(f"Se importaron {len(student_list)} estudiantes previamente guardados en {file_path}")