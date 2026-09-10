#2. Experimente con el concepto de scope:
    # Intente accesar a una variable definida dentro de una función desde afuera.

def primera_funcion(string):
    my_string = "Hola Mundo"
    print(my_string)



primera_funcion("Carlos")


    #Intente accesar a una variable global desde una función y cambiar su valor.

my_string = "Hola Mundo"
def primera_funcion():
    my_string = "Hasta pronto mundo"
    print(my_string)



print(my_string)