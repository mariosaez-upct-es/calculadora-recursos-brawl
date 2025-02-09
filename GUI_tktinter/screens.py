import tkinter as tk
from constantes import style #para cambiar solo las cosas del archivo
from prototipo_v1 import calcular_recursos_brawler
class Home(tk.Frame): #un frame es otro lienzo como la pantalla principal

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller
        #hasta aquí la base
        self.datos = tk.StringVar()
        self.salida = None
        self.salida_pantalla = tk.StringVar()
        self.init_widgets()


    
    def aplicar_calculos(self):
        datos = (self.datos.get()).split(",")
        self.salida = datos
        if len(self.salida) > 4 and self.salida[4].lower() == 'true':
            self.salida = calcular_recursos_brawler(int(self.salida[0]), int(self.salida[1]), int(self.salida[2]), int(self.salida[3]), True, int(self.salida[5]))
        else:
            self.salida = calcular_recursos_brawler(int(self.salida[0]), int(self.salida[1]), int(self.salida[2]), int(self.salida[3]), False, int(self.salida[5]))
        self.salida_pantalla.set(f"Necesitas {self.salida[0]} monedas y {self.salida[1]} puntos de fuerza")


    def init_widgets(self):
        tk.Label(
            self, 
            text = "Calculadora de Recursos BS",
            justify = tk.CENTER,
            **style.STYLE #desempaqueta el diccionario y asigna los parámetros correspondientes.
            ).pack(
                side = tk.TOP,
                fill = tk.BOTH,
                expand = True,
                padx = 22,
                pady = 11  #reducir el márgen máximo
            )
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background = style.COMPONENT)
        optionsFrame.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx=22,
            pady=11
        )
        tk.Label(
            optionsFrame,
            text = "Introduce los datos deseados (separados por ,): ",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11
        )
        tk.Entry(
            optionsFrame,
            textvariable = self.datos,
            justify= tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.Y,
            padx = 22,
            pady = 11
        )
        tk.Button(
            optionsFrame,
            text="Confirmar",
            justify= tk.CENTER,
            command= self.aplicar_calculos,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.Y,
            padx = 22,
            pady = 11            
        )
        tk.Label(
            self, 
            textvariable = self.salida_pantalla,
            justify = tk.CENTER,
            **style.STYLE 
            ).pack(
                side = tk.BOTTOM,
                fill = tk.BOTH,
                expand = True,
                padx = 22,
                pady = 11  
            )






class Game(tk.Frame): #un frame es otro lienzo como la pantalla principal

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller