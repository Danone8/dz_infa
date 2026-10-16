from tkinter import*

def calc(*args):
    try:
        result.set(str(eval(command.get())))
    except:
        pass
root = Tk()
root.title('Калькулятор')
root.geometry('600x400')  
root.minsize(300, 200)   

mainframe = Frame(root)
mainframe.grid(column = 0, row = 0, sticky = (N, S, W, E))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
mainframe.columnconfigure(1, weight=1)
command = StringVar()
result = StringVar()

entry = Entry(mainframe, textvariable = command)
entry.grid(column=1, row=0, sticky=(W, E), padx=10, pady=10)

Label(mainframe, textvariable = result).grid(column = 1, row = 2)

Button(mainframe, text = 'Calculate', command = calc).grid(column = 1, row = 3)

root.bind('<Return>', calc)
entry.focus()
root.mainloop()