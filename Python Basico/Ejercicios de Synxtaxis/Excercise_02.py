#2. Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
name = input("Ingrese su nombre: ")
last_name = input("ingrese su apellido: ")
age = int(input("ingrese su edad: "))
if(age <= 3):
    print(name + " " + last_name + " es un bebe")
elif(age > 3 and age <= 9):
    print(name + " " + last_name + " es un niño")
elif(age > 9 and age <= 13):
    print(name + " " + last_name + " es un pre-adolescente")
elif(age > 13 and age <= 20):
    print(name + " " + last_name + " es un adolescente")
elif(age > 20 and age <= 30):
    print(name + " " + last_name + " es un adulto joven") 
elif(age > 30 and age <= 65):
    print(name + " " + last_name + " es un adulto") 
elif(age > 65):
    print(name + " " + last_name + " es un adulto mayor")