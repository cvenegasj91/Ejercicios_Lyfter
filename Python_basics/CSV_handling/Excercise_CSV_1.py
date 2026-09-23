# Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
#     1. Debe incluir:
#         1. Nombre
#         2. Género
#         3. Desarrollador
#         4. Clasificación ESRB


import csv


def main():
    video_games_list = []
    while True:
        try:
            video_games_numb = int(input('Ingrese el numero de video juegos que desea ingresar: '))

            for i in range(video_games_numb):
                print(f'Ingrese video juego numero: {i+1}')
                name = input('Nombre: ')
                gender = input('Genero: ')
                developer = input('Desarrollador: ')
                rating = input('Clasificacion ESRB: ')

                video_games_dic = {
                    'nombre': name, 
                    'genero': gender, 
                    'desarrollador': developer, 
                    'clasificacion ESRB': rating
                    }
                video_games_list.append(video_games_dic)       

            write_csv_file('Video_juegos.csv', video_games_list, video_games_list[0].keys())
            break

        except ValueError as e:
            print(f'Ingresar una cantidad valida: {e}') 

        except IndexError as e:
            print(f'Ingrese una cantidad posistiva: {e}')


def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8', newline = '') as file:
        writer = csv.DictWriter(file, headers,)
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    main()