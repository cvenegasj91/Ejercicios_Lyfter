# 1. Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON ([Archivos JSON](https://www.notion.so/Archivos-JSON-79f9758cb59d4452a9c8668efa25356c?pvs=21)).
#     1. Debe leer el archivo para importar los Pokémones existentes.
#     2. Luego debe pedir la información del Pokémon a agregar.
#     3. Finalmente debe guardar el nuevo Pokémon en el archivo.

import json


def load_pokemons(path):
    try:
        with open(path, encoding='utf-8') as file:
            pokemon_dict = json.load(file)
            return pokemon_dict
    except FileNotFoundError as e:
        print(f'Archivo no encontrado: {e}')        


def new_pokemon_inputs():
    print('---Ingresar datos del nuevo pokemon---')
    name = input('Ingrese el nombre: ')
    kind = input('Ingrese el tipo: ').split(",")
    kind = [i.strip() for i in kind]

    print('Base:')
    hp = int(input('HP: '))
    attack = int(input('Attack: '))
    defense = int(input('Defense: '))
    sp_attack = int(input('Sp. Attack: '))
    sp_defense = int(input('Sp. Defense: '))
    speed = int(input('Speed: '))

    new_pokemon = {
        "name": {"english": name},
        "type": [kind],
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }
    return new_pokemon


def save_new_pokemon(path, new_pokemon):
    with open(path, 'w', encoding= 'utf-8') as file:
        json.dump(new_pokemon, file, indent=4)


def main():
    path = 'pokemon_list.json'
    pokemons = load_pokemons(path)
    new_pokemon = new_pokemon_inputs()
    pokemons.append(new_pokemon)
    save_new_pokemon(path, pokemons)


if __name__ == '__main__':
    main()