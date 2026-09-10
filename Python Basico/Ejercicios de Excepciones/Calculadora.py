def calculator(option, a, b):
        if option == 1:
            return a + b
        elif option == 2:
            return a - b
        elif option == 3:
            return a * b
        elif option == 4:
            try:
                return a / b
            except ZeroDivisionError as error:
                print(f"No se puede dividir por 0: {error}")
                return a


def show_menu():
    print("Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Borrar resultado")
    print("6. Salir")


def main():
    current_numb = 0.0
    while True:
        show_menu()
        try:
            option = int(input("Ingrese operacion (1/2/3/4/5/6): "))
            if option == 6:
                print("Saliendo de la calculadora")
                break
            elif option == 5:
                current_numb = 0.0
                print(f"Numero reiniciado: {current_numb}")
            elif option in [1, 2, 3, 4]:
                print(f'Numero actual {current_numb}')
                new_numb = float(input('Ingrese nuevo numero: '))
                current_numb = calculator(option, current_numb, new_numb)
                print(f"Resultado: {current_numb}")
            else:
                print("Ingrese una opcion valida del 1 al 6")
        except ValueError as error:
            print(f"Ingrese un valor valido: {error}")


if __name__ == '__main__':
    main()