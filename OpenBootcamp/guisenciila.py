import tkinter
from tkinter import ttk


window = tkinter.Tk()

username_label = ttk.Label(window ,text="Aprendiendo GUI en Python :)")
username_label.grid(column=0, row=0 ,sticky=tkinter.W, padx=5, pady=5)

listbox = tkinter.Listbox(window, height = 10)
listbox.grid(column=0, row=1, sticky=tkinter.W)
listbox.insert(tkinter.END,"Python","Java", "C++", "C", "Go", "Dart", "Javascript")

window.mainloop()   
