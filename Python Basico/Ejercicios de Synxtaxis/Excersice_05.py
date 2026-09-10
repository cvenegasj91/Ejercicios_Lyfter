#5. Dada `n` cantidad de notas de un estudiante, calcular:
    # 1. Cuantas notas tiene aprobadas (mayor a 70).
    # 2. Cuantas notas tiene desaprobadas (menor a 70).
    # 3. El promedio de todas.
    # 4. El promedio de las aprobadas.
    # 5. El promedio de las desaprobadas.

total_grades = int(input("Ingrese cantidad de notas: "))
total_failed_grades = 0
failed_grades_average = 0
total_approved_grades = 0
approved_grades_average = 0
total_grades_average = 0
grades_counter = 1
while grades_counter <= total_grades:
    current_grade = int(input(f'Ingrese la nota numero {grades_counter}: '))
    grades_counter = grades_counter +1
    if(current_grade < 70):
        total_failed_grades = total_failed_grades + 1
        failed_grades_average = failed_grades_average + current_grade
    else:
        total_approved_grades = total_approved_grades + 1
        approved_grades_average = approved_grades_average + current_grade
    total_grades_average = total_grades_average + (current_grade / total_grades)
if(total_failed_grades > 0):
    failed_grades_average /= total_failed_grades
else:
    failed_grades_average = 0
if(total_approved_grades > 0):
    approved_grades_average /= total_approved_grades
else:
    approved_grades_average = 0
print(f'El estudiante tiene esta cantidad de notas aprobadas: {total_approved_grades}')
print(f'Este es el promedio de notas aprobadas: {approved_grades_average}')
print(f'El estudiante tiene esta cantidad de notas desaprobadas: {total_failed_grades}')
print(f'Este es el promedio de notas desaprobadas {failed_grades_average}')
print(f'Este es el promedio total de notas: {total_grades_average}')