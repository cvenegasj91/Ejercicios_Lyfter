#Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def sort_songs(original_list, sorted_list):
    try:
        with open(original_list, encoding= 'utf-8') as file:
            songs = file.readlines()

        songs.sort()

        with open(sorted_list, 'w', encoding= 'utf=8') as new_file:
            for song in songs:
                new_file.write(song)
                print(song.strip())
    
    except FileNotFoundError as e:
        print(f'El archivo no existe: {e}')

sort_songs('songs_list.txt', 'new_songs_list.txt')