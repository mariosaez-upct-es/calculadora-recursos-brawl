import tkinter as tk
from constantes import style
from screens import Home, Game

class Manager(tk.Tk): #hereda de la clase principal de Tkinter, lo que crea la pantallita principal

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #coge el init de la superclase
        self.title("Calculadora de Recursos BS")
        container = tk.Frame(self) #Este frame será el parent de los demás widgets, incluidos frames.
        container.pack(
            side = tk.TOP,
            fill = tk.BOTH, #se expande a la par de la ventana
            expand = True
        )
        container.configure(background= style.BACKGROUND) #configuramos el fondo
        container.grid_columnconfigure(0, weight= 1)
        container.grid_rowconfigure(0, weight=1)
        ## Son los índices de las filas y las columnas. El peso es lo que ocupa respecto a los demás widgets

        self.frames = {}
        for F in (Home, Game):
            frame = F(container, self) #container es el frame que lo va a contener todo
            #el container será el parent de Home y Game y el controller, la aplicación inicial.
            self.frames[F] = frame #guardamos los frames
            frame.grid(row = 0, column = 0, sticky = tk.NSEW)
        self.show_frame(Home) #inicia en home

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise() #va alternando los frames, para poder pasar pantallas