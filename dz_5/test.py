from tkinter import *
root = Tk()
root.title('Приложение')
root.geometry('300x300')

label = Label(root, text = 'Hello')
label.pack(side = 'bottom')
root.mainloop()