#Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

my_list = [10, 20, 30, 40, 50,]

if len(my_list) < 2:
    print(my_list)
my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(f'Lista mofidicada: {my_list}')