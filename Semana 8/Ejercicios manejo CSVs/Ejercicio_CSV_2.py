#Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.

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

            write_tsv_file('Video_juegos.tsv', video_games_list, video_games_list[0].keys())
            break

        except ValueError as e:
            print(f'Ingresar una cantidad valida: {e}') 

        except IndexError as e:
            print(f'Ingrese una cantidad posistiva: {e}')


def write_tsv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8', newline = '') as file:
        writer = csv.DictWriter(file, headers, delimiter= '\t')
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    main()