#3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
    # Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.
number = int(input("Adivine un numero del 1 al 10: "))
import random
secret_number = random.randint(1, 10)
if(number >10):
    print("Numero fuera del rango")
elif(number >= 1 and number <= 10):
    while number != secret_number:
        print("Numero incorrecto")
        number = int(input("Adivine un numero del 1 al 10: "))
if(number == secret_number):
    print("Felcidades, adivino el numero secreto!")