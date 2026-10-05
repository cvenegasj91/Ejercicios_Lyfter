# 5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#     1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”


def lowers_capitatls_counter(text):
    capital_cases = 0
    lower_cases = 0

    if not isinstance(text, str):
        raise TypeError("Enter a String")
    
    for character in text:
        code = ord(character)

        if (65 <= code <= 90) or code in [193, 201, 205, 211, 218, 209]:     
            capital_cases += 1
        elif (97 <= code <= 122) or code in [225, 233, 237, 243, 250, 241]:  
            lower_cases += 1

    return capital_cases, lower_cases