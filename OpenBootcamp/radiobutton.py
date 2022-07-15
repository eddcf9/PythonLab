import tkinter
from tkinter import ttk

window = tkinter.Tk()

label = ttk.Label(window, text="ELige tu animal favorito")
label.grid(column=0, row=0, sticky=tkinter.W, padx=55, pady=55)

seleccionado = tkinter.StringVar()
seleccionado2 = tkinter.StringVar()
seleccionado3 = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="Leon", value=1, variable=seleccionado)
r1.grid(column=0, row=1, padx=55, pady=55)
r2 = ttk.Radiobutton(window, text="Jirafa", value=1, variable=seleccionado2)
r2.grid(column=0, row=2, padx=55, pady=55)
r3 = ttk.Radiobutton(window, text="Tiburon", value=1, variable=seleccionado3)
r3.grid(column=0, row=3, padx=55, pady=55)

def leon(event):
    print("Has seleccionado al Leon")
r1.bind('<Button-1>', leon)
def jirafa(event):
    print("Has seleccionado la jirafa")
r2.bind('<Button-1>', jirafa)
def tiburon(event):
    print("Has seleccionado el tiburon")
r3.bind('<Button-1>', tiburon)

def resetFields(event):
    seleccionado.set(None)
    seleccionado2.set(None)
    seleccionado3.set(None)

boton = ttk.Button(window, text="Reiniciar")
boton.grid(column=0, row=4, sticky=tkinter.N, padx=5, pady=5)
boton.bind('<Button-1>', resetFields)


window.mainloop()

