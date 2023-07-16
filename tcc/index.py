from tkinter import *
from tkinter.ttk import *
import py
import subprocess as sub


def get_idioma():
    pegar = mudar_idioma.get()
    if pegar == "English":
        window.destroy()
        sub.call("python index_en.py", shell=True)


lista_idiomas = ["Portuguese", "English"]
window = Tk()
window.title("Menu")

texto = Label(window, text="Athess")
texto.pack()

enviar = Button(window, text="Enviar e-mail", command=py.printar)
enviar.pack()

criar = Button(window, text="Criar gráfico", command=py.printar)
criar.pack()

mudar_idioma = Combobox(window, values=lista_idiomas)
mudar_idioma.pack()

choose = Button(window, text="Enviar", command=get_idioma)
choose.pack()
window.mainloop()
