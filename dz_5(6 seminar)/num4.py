from tkinter import *


def calc(*args):
    color = command.get().strip()

    if len(color) != 7 or color[0] != '#':
        result.set('Введите цвет в формате #XXYYZZ')
        return
    if any(symbol not in '0123456789abcdefABCDEF' for symbol in color[1:]):
        result.set('Используйте цифры 0–9 и буквы A–F')
        return
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:7], 16)

    complementary = f'#{255 - r:02x}{255 - g:02x}{255 - b:02x}'

    result.set(complementary)
    original_color.config(bg=color)
    comp_color.config(bg=complementary)


root = Tk()
root.title('Подбор цветов')
root.geometry('520x340')
root.minsize(480, 340)

mainframe = Frame(root, padx=15, pady=15)
mainframe.grid(column=0, row=0, sticky=(N, S, W, E))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.rowconfigure(4, weight=1)

command = StringVar()
result = StringVar()

Label(mainframe, text='Подбор комплементарного цвета', font=('Arial', 14, 'bold')).grid(column=0, row=0, columnspan=2, pady=(0, 15))
Label(mainframe, text='Цвет в формате HEX').grid(column=0, row=1, sticky=W, padx=5, pady=5)

entry_color = Entry(mainframe, textvariable=command)
entry_color.grid(column=1, row=1, sticky=(W, E), padx=5)

Button(mainframe, text='Подобрать цвет', command=calc).grid(column=0, row=2, columnspan=2, pady=15)
Label(mainframe, text='Исходный цвет').grid(column=0, row=3, padx=5, pady=5)
Label(mainframe, text='Комплементарный цвет').grid(column=1, row=3, padx=5, pady=5)

original_color = Label(mainframe, bg='white', relief='solid', bd=1)
original_color.grid(column=0, row=4, sticky=(N, S, W, E), padx=5, pady=5)

comp_color = Label(mainframe, bg='white', relief='solid', bd=1)
comp_color.grid(column=1, row=4, sticky=(N, S, W, E), padx=5, pady=5)

Label(mainframe, textvariable=result).grid(column=0, row=5, columnspan=2, pady=10)

root.bind('<Return>', calc)
entry_color.focus()
root.mainloop()