# 4. Cree una función que le de la vuelta a un string y lo retorne. # type: ignore
#     1. Esto ya lo hicimos en iterables.
#     2. “Hola mundo” → “odnum aloH”

def revert_list(my_string):
    if not isinstance(my_string, str):
        raise TypeError("Invalid input")
    
    return my_string[:: -1]