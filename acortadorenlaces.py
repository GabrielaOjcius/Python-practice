import pyshorteners
from tkinter import *
from tkinter import ttk
import webbrowser
import pyperclip

ventana = Tk() 
ventana.minsize(400, 310)
ventana.title("Acortador de enlaces")
ventana.resizable(0,0)

s = pyshorteners.Shortener()

def acortamiento():
    acortado = s.tinyurl.short(acortar_entry.get())
    resultado_label = Label(ventana, text=acortado)
    resultado_label.grid(row=8, column=0)
    resultado_label.config(
        fg="black",
        bg="#16a596",
        font=("Arial", 20),
        padx=210,
        pady=20
        )

    boton = Button(ventana, text="Abrir enlace", command=abrir_enlace)
    boton.grid(row=9, column=0)    
    
    boton = Button(ventana, text="Copiar enlace", command=copiar_enlace)
    boton.grid(row=10, column=0)   

def abrir_enlace():
    webbrowser.open(s.tinyurl.short(acortar_entry.get()))

def copiar_enlace():
    pyperclip.copy(s.tinyurl.short(acortar_entry.get()))


home_label = Label(ventana, text="¡Acortador de enlaces!")
home_label.config(
        fg="white",
        bg="#898b8a",
        font=("Candara", 30),
        padx=210,
        pady=20
    )
home_label.grid(row=0, column=0)


acortar_label = Label(ventana, text="Ingresá el enlace", bg="#16a596")
acortar_entry = Entry(ventana)
acortar_label.grid(row=1, column=0, padx=5, pady=5)
acortar_entry.grid(row=2, column=0, padx=5, pady=5)

boton = Button(ventana, text="¡Acortar! ✂", command=acortamiento)
boton.grid(row=6, column=0)

ventana.configure(bg='#16a596')
ventana.mainloop()