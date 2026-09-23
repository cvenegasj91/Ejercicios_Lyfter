# 4. Cree una función que le de la vuelta a un string y lo retorne. # type: ignore
#     1. Esto ya lo hicimos en iterables.
#     2. “Hola mundo” → “odnum aloH”

def revert_list(my_string):
    return my_string[:: -1]
      

invert_string = revert_list("Hola mundo")    

print(invert_string)