# 2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
#     1. Ejemplos:
#     2. `list_a = [’first_name’, ‘last_name’, ‘role’]`
#     `list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]`
#     → `{’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}`


first_list = ["name", "Age", "Occupancy"]
second_list = ["Carlos", 34, "Developer"]
first_dictionary = {}

for i in range(len(first_list)):
    first_dictionary[first_list[i]] = second_list[i]
print(first_dictionary)