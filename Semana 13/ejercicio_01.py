#Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def show_parameters(func):
    def wrapper(*args, **kwargs):
        print(f'Mostrando los parametros de la funcion {func.__name__}:')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')

        result = func(*args, **kwargs)

        print(f'Retorno de la funcion {func.__name__}: {result}')
        
        return result
    
    return wrapper


@show_parameters
def suma(a, b):
    return a + b

@show_parameters
def personal_data(name, last_name="Venegas", age=34, gender="Masculino"):
    return f'Datos personales: {name}, {last_name}, {age}, {gender}'

suma(5, 3)

personal_data('Carlos', last_name='Venegas', age=34, gender="Masculino")
