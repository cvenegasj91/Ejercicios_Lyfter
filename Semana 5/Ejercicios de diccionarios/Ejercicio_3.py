# 3. Cree un programa que use una lista para eliminar keys de un diccionario.
#     1. Ejemplos:
#     2. `list_of_keys = [’access_level’, ‘age’]`
#     `employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}`
#     → `{’name’: ‘John’, 'email’: ‘john@ecorp.com’}`


first_dictionary = {
    "name" : "Carlos",
    "age" : 34,
    "occupancy" : "Developer",
    "location" : "Quepos"
}
deleted_items = ["age", "location"]
for key in deleted_items:
    first_dictionary.pop(key)
print(first_dictionary)
print(deleted_items)