'''
import random
from re import T
import sys
import tkinter
from tkinter import Listbox, ttk

window = tkinter.Tk()


label_saludo = tkinter.Label(window, text="Hola mundo!", bg="blue", fg="yellow")

#Geometria pack, se adapta al tamaño de la ventana por default
label_saludo.pack(ipadx=50, ipady=50, fill="both") #Para cambiar tamaño
#expand = True centrarlo y expandirlo
#side = "left", "center" posicion a la izquierda
#fill = "x" hacerse hacia un lado

'''
'''
(0,0) (1,0) (2,0)
Label Entry (2,1)
Label Entry (2,2)



window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

#Frames 

frame = ttk.Frame(window)
label = ttk.Label(frame, text="Hola")
label.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=50)
frame.grid(column=0, row=0, sticky=tkinter.W)



#Label y entry de username
username_label = ttk.Label(window, text="username")
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

username_entry = ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

#Label y entry de contraseña
password_label = ttk.Label(window, text="password")
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

password_entry = ttk.Entry(window, show="*")
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

#Boton
login_button = ttk.Button(window, text="Login")
login_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)


#Colores aleatorios

colors = ["blue", "red", "yellow", "purple", "green", "black"]

for x in range(0, 10):
    color = random.randint(0, len(colors)-1)
    color2 = random.randint(0, len(colors)-1)
    label = tkinter.Label(window, text="Etiqueta", bg=colors[color], fg=colors[color2])
    label.place(x=random.randint(0,100), y=random.randint(0,100))


window.mainloop()

lista = ["windows", "linux"]
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height = 100, listvariable=lista)
listbox.grid(column=0, row=0, sticky=tkinter.W)


seleccionado = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="Si", value=1, variable=seleccionado)
r1.grid(column=0, row=1, padx=5, pady=5)


def mifuncion():
    print("Hola")
seleccionado2 = tkinter.StringVar()
checkbox = ttk.Checkbutton(window, text="Acepto las condiciones", variable=seleccionado2, command=mifuncion)
checkbox.grid(row=0, column=0)


#Evento
def saludar(event):
    print("Saludo")

def salir(evento):
    window.quit()

boton = tkinter.Button(window, text="Has click")
boton.pack()
boton.bind('<Button-1', saludar)
boton.bind('<Double-1', saludardoble)
#<motion> te marca la posicion del puntero en timpo real

'''