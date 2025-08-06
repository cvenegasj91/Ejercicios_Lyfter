# 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#     1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#     2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”


def sort_words_AZ(text):
    word_list = []
    word = ""

    for character in text:
        if character != "-":
            word += character
        else:
            word_list.append(word)
            word = ""
    word_list.append(word)

    for i in range(len(word_list)):
        for j in range(i +1, len(word_list)):
            if word_list[j] < word_list[i]:
                word = word_list[i]
                word_list[i] = word_list[j]
                word_list[j] = word
    
    result = ""
    for i in range(len(word_list)):
        result += word_list[i]
        if i < len(word_list) - 1:
            result += "-"

    return result


sentence =  "pera-manzana-mango-zanahoria-aguacate-limon-sandia-papaya"
print(sort_words_AZ(sentence))