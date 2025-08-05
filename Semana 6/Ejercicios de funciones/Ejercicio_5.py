# 5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#     1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”


def lowers_capitatls_counter(text):
    capital_cases = 0
    lower_cases = 0

    for character in text:
        code = ord(character)
        if 65 <= code <= 90:     
            capital_cases += 1
        elif 97 <= code <= 122:  
            lower_cases += 1

    return capital_cases, lower_cases


sentece = "El Mundo Es Genial"
upper, lower = lowers_capitatls_counter(sentece)

print(sentece)
print(f'Numero de mayusculas es {upper} y el numero de minusculas es {lower}')