from tkinter import *
import pandas as pd
import random


def choose_film(*args):
    genre = command.get().strip().lower()

    if genre == '':
        result.set('Введите жанр')
        return

    suitable_films = []

    for i in films.index:
        genres = films.loc[i, 'Genre'].lower().split(' | ')

        if genre in genres:
            suitable_films.append(i)

    if len(suitable_films) == 0:
        result.set('Фильмы такого жанра не найдены')
        return

    i = random.choice(suitable_films)
    title = films.loc[i, 'Title']
    year = films.loc[i, 'Year']
    result.set(f'{title} ({year})')


films = pd.read_csv('imdb_top_250.csv')
film_genres_list = list(films['Genre'])

complex_genres = []

for film_genre in film_genres_list:
    genres = film_genre.split(' | ')

    if len(genres) > 1:
        for genre in genres:
            film_genres_list.append(genre)

        complex_genres.append(film_genre)

for genre in complex_genres:
    film_genres_list.remove(genre)

genres_set = set(film_genres_list)

root = Tk()
root.title('Фильмотека')
root.geometry('600x350')
root.minsize(600, 350)

mainframe = Frame(root, padx=15, pady=15)
mainframe.grid(column=0, row=0, sticky=(N, S, W, E))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)

command = StringVar()
result = StringVar()

Label(mainframe, text='Случайный фильм по жанру', font=('Arial', 14, 'bold')).grid(column=0, row=0, columnspan=2, pady=(0, 15))
Label(mainframe, text='Жанр').grid(column=0, row=1, sticky=W, padx=5, pady=5)

entry_genre = Entry(mainframe, textvariable=command)
entry_genre.grid(column=1, row=1, sticky=(W, E), padx=5)
Button(mainframe, text='Выбрать фильм', command=choose_film).grid(column=0, row=2, columnspan=2, pady=15)
Label(mainframe, textvariable=result, font=('Arial', 12, 'bold'), wraplength=540).grid(column=0, row=3, columnspan=2, pady=10)
Label(mainframe, text='Доступные жанры: ' + ', '.join(sorted(genres_set)), wraplength=540, justify=LEFT).grid(column=0, row=4, columnspan=2, sticky=W, padx=5, pady=10)

root.bind('<Return>', choose_film)
entry_genre.focus()
root.mainloop()