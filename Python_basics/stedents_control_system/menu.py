def show_menu():
    print("--Sistema de control de estudiantes--")
    print("1-Ingresar informacion de estudiantes")
    print("2-Ver informacion de estudiantes ingresados")
    print("3-Ver top 3 de mejores promedios")
    print("4-Ver nota promedio entre todas las notas promedio")
    print("5-Exportar archivo CSV con datos guardados")
    print("6-Importar datos guardado en archivo CSV")
    print("7-Salir")

    while True:
        try:
            opt = int(input("Ingrese una opcion: "))
            if opt in (1, 2, 3, 4, 5, 6, 7):
                return opt
            print("Ingrese una opcion del valida del menu")
        except ValueError as e:
            print("Valor no valido, intente de nuevo")
