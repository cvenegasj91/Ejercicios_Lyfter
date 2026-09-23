#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

def verify_prime_numb(numb):
    if numb <= 1:
        return False
    for i in range(2, numb):
        if numb % i == 0:
            return False
    return True


def calculate_prime_numb(numb_list):
    prime_numb_list = []
    for i in numb_list:
        if verify_prime_numb(i):
            prime_numb_list.append(i)
    return prime_numb_list


prueba = [3, 1, 2, 6, 9, 45, 79, 63, 17, 41, 13]
print(calculate_prime_numb(prueba))