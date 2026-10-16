from tkinter import *


def calc(*args):
    result.set('')
    interpretation.set('')

    try:
        m = float(mass.get().replace(',', '.'))
        h = float(height.get().replace(',', '.'))

        if m <= 0 or h <= 0:
            pass

        h = h / 100
        bmi = m / h**2
        result.set(f'{bmi:.2f}')

        if bmi <= 16:
            interpretation.set('Выраженный дефицит массы тела')
        elif bmi < 18.5:
            interpretation.set('Недостаточная масса тела')
        elif bmi < 25:
            interpretation.set('Норма')
        elif bmi < 30:
            interpretation.set('Избыточная масса тела (предожирение)')
        elif bmi < 35:
            interpretation.set('Ожирение 1 степени')
        elif bmi < 40:
            interpretation.set('Ожирение 2 степени')
        else:
            interpretation.set('Ожирение 3 степени')

    except ValueError:
        pass


root = Tk()
root.title('Калькулятор индекса массы тела')
root.geometry('520x300')
root.minsize(480, 300)

mainframe = Frame(root, padx=15, pady=15)
mainframe.grid(column=0, row=0, sticky=(N, S, W, E))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)

mass = StringVar()
height = StringVar()
result = StringVar()
interpretation = StringVar()

Label(mainframe, text='Калькулятор индекса массы тела', font=('Arial', 14, 'bold')).grid(column=0, row=0, columnspan=3, pady=(0, 15))
Label(mainframe, text='Масса').grid(column=0, row=1, sticky=W, padx=5, pady=5)

entry_mass = Entry(mainframe, textvariable=mass)
entry_mass.grid(column=1, row=1, sticky=(W, E), padx=5)

Label(mainframe, text='кг').grid(column=2, row=1, sticky=W, padx=5)
Label(mainframe, text='Рост').grid(column=0, row=2, sticky=W, padx=5, pady=5)

entry_height = Entry(mainframe, textvariable=height)
entry_height.grid(column=1, row=2, sticky=(W, E), padx=5)

Label(mainframe, text='см').grid(column=2, row=2, sticky=W, padx=5)
Label(mainframe, text='ИМТ').grid(column=0, row=3, sticky=W, padx=5, pady=5)
Label(mainframe, textvariable=result).grid(column=1, row=3, sticky=W, padx=5)
Label(mainframe, text='кг/м²').grid(column=2, row=3, sticky=W, padx=5)
Button(mainframe, text='Рассчитать', command=calc).grid(column=0, row=4, columnspan=3, pady=15)
Label(mainframe, textvariable=interpretation, wraplength=420).grid(column=0, row=5, columnspan=3, pady=10)

root.bind('<Return>', calc)
entry_mass.focus()
root.mainloop()