#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for i, value in enumerate(args):
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError(
                    f"El parametro {i} no es numerico: {value} ({type(value).__name__})"
                )
            
        for name, value in kwargs.items():
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError(
                    f"El parametro {name} no es numerico: {value} ({type(value).__name__})"
                )
            
        return func(*args, **kwargs)
    
    return wrapper



@validate_numbers
def sum(a, b):
    return a + b


print(sum(10,"5"))
