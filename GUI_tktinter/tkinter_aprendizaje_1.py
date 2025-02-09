import tkinter as tk

app = tk.Tk()
app.geometry("400x200")  # Tamaño de la ventana. Ancho x Alto
app.configure(bg="black")  # Color de fondo de la ventana, tiene más parámetros que se pueden configurar.
tk.WM.wm_title(app, "Calculadora de recursos Brawl Stars")  # Título de la ventana, se llama al método wm_title de la clase WM. Windows Manager.

# A la hora de crear widgets, hay que especificar dónde se va a incrustar y cómo se va a incrustar.
## Para la primera cuestión, se especifica en la creación del widget, como primer argumento.
## Para la segunda cuestión, se especifica mediante el método pack() o grid().
### Además, pack() especifica cómo se ajusta el widget al contenedor, si a ambos lados de la pantalla, si a uno solo y si se quiere que se expanda si se expande el padre.

#En el widget, con la opción command se puede especificar una función que se ejecute al hacer click en el botón. La función se le pasa como objeto, sin paréntesis.

### Si se designan varios widgets con la misma configuración en pack(), se repartirán el espacio disponible entre ellos. Si no se limitan los límites superiores, se dividen en un % equivalente.

### Lo importante: Las Entry son los widgets que permiten al usuario introducir texto en el programa.
#### --->   Se definirá una variable que recogerá el texto introducido en la Entry. Para que otras instancias puedan acceder a la palabra, se debe usar el metodo get() de la variable.
#### --->   Gracias a mainloop, cada vez que se modifique la entrada, se verá reflejado en las interacciones del programa
#### --->   También se puede modificar el texto de alguna otra variable de manera interna usando la palabra de Entry, por ejemplo.
### Si se define un texto y una textvariable, la textvariable se superpone al texto. Si se modifica la textvariable, se modifica el texto del widget.



app.mainloop()  # Va refrescando la aplicación para que se vean los cambios que se vayan generando. Recoge los eventos y los modifica según se programe.