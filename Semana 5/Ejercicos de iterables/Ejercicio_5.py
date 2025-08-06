#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

number_list = []
print("ingrese 10 numeros:")

for i in range(10):
    numb = int(input(f"Número {i+1}: "))
    number_list.append(numb)

largest_numb = number_list[0]
for number in number_list:
    if number > largest_numb:
        largest_numb = number

print(f'Números ingresados:  {number_list}')
print(f'Número más alto: {largest_numb}')