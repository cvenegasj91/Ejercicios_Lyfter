#4. Cree un programa que le pida tres números al usuario y muestre el mayor.
number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))
number3 = int(input("Ingrese el tercer numero: "))
if(number1 > number2 and number1 > number3):
    print(f'El numero mayor es: {number1}')
elif(number2 > number1 and number2 > number3):
    print(f'El numero mayor es: {number2}')
elif(number3 > number1 and number3 > number2):
    print(f'El numero mayor es: {number3}')