# 3. Cree una función que retorne la suma de todos los números de una lista.
#     1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).

def sum_numbers(list_of_numb = [20, 35, 40, 25, 30, 15]):
    sum = 0
    for numb in list_of_numb:
        sum = sum + numb
    return sum


print(sum_numbers())