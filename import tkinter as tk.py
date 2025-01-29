import tkinter as tk
from tkinter import ttk
import random

# Clase que representa una celda del tablero
class Celda:
    def __init__(self, x, y, boton):
        self.x = x  # Coordenada x de la celda
        self.y = y  # Coordenada y de la celda
        self.boton = boton  # Botón asociado a la celda en la interfaz
        self.tiene_mina = False  # Indica si la celda tiene una mina
        self.revelada = False  # Indica si la celda ha sido revelada
        self.marcada = False  # Indica si la celda ha sido marcada con una bandera
        self.numero_adyacente = 0  # Número de minas adyacentes a la celda

# Clase que representa el juego de Buscaminas
class Buscaminas:
    def __init__(self, root, filas=9, columnas=9, minas=10):
        self.root = root  # Ventana principal de la aplicación
        self.filas = filas  # Número de filas del tablero
        self.columnas = columnas  # Número de columnas del tablero
        self.minas = minas  # Número de minas en el tablero
        self.celdas = []  # Lista de celdas del tablero
        self.crear_interfaz()  # Crear la interfaz gráfica
        self.crear_tablero()  # Crear el tablero de juego
        self.colocar_minas()  # Colocar las minas en el tablero
        self.calcular_numeros_adyacentes()  # Calcular los números adyacentes a cada celda

    # Crear la interfaz gráfica
    def crear_interfaz(self):
        self.ventana = tk.Tk()
        self.ventana.title("Buscaminas")
        self.ventana.geometry("600x400")
        self.ventana.iconbitmap("img/icono.ico")
        self.ventana.minsize(600, 400)
        self.ventana.maxsize(600, 400)

        # Encabezado
        self.encabezado = tk.Frame(self.ventana, relief=tk.RAISED, borderwidth=2)
        self.encabezado.pack(side=tk.TOP, fill=tk.X)

        # Título del juego
        self.titulo = tk.Label(self.encabezado, text="BUSCAMINAS", font=("Arial", 16), fg="darkgreen")
        self.titulo.pack(side=tk.LEFT, padx=10)

        # Selector de dificultad
        self.dificultad_label = tk.Label(self.encabezado, text="Dificultad", font=("Arial", 10))
        self.dificultad_label.pack(side=tk.LEFT, padx=10)

        self.dificultad_selector = ttk.Combobox(self.encabezado, values=["Principiante", "Intermedio", "Experto"], state="readonly")
        self.dificultad_selector.set("Principiante")
        self.dificultad_selector.pack(side=tk.LEFT)
        self.dificultad_selector.bind("<<ComboboxSelected>>", )

        # Contador de minas restantes
        self.minas_frame = tk.Frame(self.encabezado)
        self.minas_frame.pack(side=tk.LEFT, padx=20)

        self.bandera_icono = tk.Label(self.minas_frame, text="\u2691", font=("Arial", 16), fg="red")  # Icono de bandera
        self.bandera_icono.pack(side=tk.LEFT)

        self.minas_restantes = tk.Label(self.minas_frame, text="99", font=("Arial", 14)) # VALOR VARIA SEGUN DIFICUKTAD Y DISMINUYE AL PONER UNA BANDERA
        self.minas_restantes.pack(side=tk.LEFT, padx=5)

        # Temporizador
        self.temporizador = tk.Label(self.encabezado, text="00:00", font=("Arial", 14), relief=tk.SUNKEN, width=6) #TEMPORIZADOR QUE SUMA VALOR CADA SEGUNDO
        self.temporizador.pack(side=tk.RIGHT, padx=20)

        # Puntajes
        self.puntajes_frame = tk.Frame(self.ventana, relief=tk.SUNKEN, borderwidth=2)
        self.puntajes_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.record_label = tk.Label(self.puntajes_frame, text="RECORD:", font=("Arial", 12)) #DEBE HABER UN RECORD POR CADA DIFICULTAD
        self.record_label.pack(pady=5)

        self.record_puntos = tk.Label(self.puntajes_frame, text="", font=("Arial", 12), relief=tk.SUNKEN, width=12)
        self.record_puntos.pack(pady=5)

        # Tablero de cuadrículas
        self.frame_tablero = tk.Frame(self.ventana, relief=tk.SUNKEN, borderwidth=2)
        self.frame_tablero.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)


    # Crear el tablero de juego
    def crear_tablero(self):
        for x in range(self.filas):
            fila = []
            for y in range(self.columnas):
                # Crear un botón para cada celda
                boton = tk.Button(self.frame_tablero, width=3, height=1, command=lambda x=x, y=y: self.revelar_celda(x, y))
                boton.bind("<Button-3>", lambda e, x=x, y=y: self.marcar_celda(x, y))  # Asociar el botón derecho del ratón para marcar la celda
                boton.grid(row=x, column=y)  # Colocar el botón en la cuadrícula
                fila.append(Celda(x, y, boton))  # Añadir la celda a la fila
            self.celdas.append(fila)  # Añadir la fila al tablero

    # Colocar las minas en el tablero
    def colocar_minas(self):
        # Seleccionar posiciones aleatorias para las minas
        posiciones = random.sample([(x, y) for x in range(self.filas) for y in range(self.columnas)], self.minas)
        for x, y in posiciones:
            self.celdas[x][y].tiene_mina = True  # Colocar una mina en la celda seleccionada

    # Calcular los números adyacentes a cada celda
    def calcular_numeros_adyacentes(self):
        for x in range(self.filas):
            for y in range(self.columnas):
                if not self.celdas[x][y].tiene_mina:
                    self.celdas[x][y].numero_adyacente = self.contar_minas_adyacentes(x, y)  # Contar las minas adyacentes

    # Contar las minas adyacentes a una celda
    def contar_minas_adyacentes(self, x, y):
        direcciones = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # Direcciones de las celdas adyacentes
        minas = 0
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.filas and 0 <= ny < self.columnas and self.celdas[nx][ny].tiene_mina:
                minas += 1  # Incrementar el contador si hay una mina adyacente
        return minas

    # Revelar una celda
    def revelar_celda(self, x, y):
        celda = self.celdas[x][y]
        if celda.revelada or celda.marcada:
            return

        celda.revelada = True
        if celda.tiene_mina:
            self.game_over(perdio=True)  # Terminar el juego si se revela una mina
            return

        # Mostrar el número de minas adyacentes o dejar vacío si no hay minas adyacentes
        celda.boton.config(text=str(celda.numero_adyacente) if celda.numero_adyacente > 0 else "", state="disabled")

        if celda.numero_adyacente == 0:
            self.revelar_en_cascada(x, y)  # Revelar en cascada si no hay minas adyacentes

        self.verificar_victoria()  # Verificar si se ha ganado el juego

    # Revelar celdas en cascada
    def revelar_en_cascada(self, x, y):
        direcciones = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # Direcciones de las celdas adyacentes
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.filas and 0 <= ny < self.columnas:
                self.revelar_celda(nx, ny)  # Revelar la celda adyacente

    # Marcar una celda con una bandera
    def marcar_celda(self, x, y):
        celda = self.celdas[x][y]
        if celda.revelada:
            return

        if celda.marcada:
            celda.boton.config(text="")  # Quitar la marca si ya está marcada
        else:
            celda.boton.config(text="F")  # Marcar la celda con una bandera

        celda.marcada = not celda.marcada  # Cambiar el estado de marcada

    # Verificar si se ha ganado el juego
    def verificar_victoria(self):
        for fila in self.celdas:
            for celda in fila:
                if not celda.tiene_mina and not celda.revelada:
                    return
        self.game_over(perdio=False)  # Terminar el juego si se han revelado todas las celdas sin minas

    # Terminar el juego
    def game_over(self, perdio):
        for fila in self.celdas:
            for celda in fila:
                if celda.tiene_mina:
                    celda.boton.config(text="*", state="disabled")  # Mostrar todas las minas
                celda.boton.config(state="disabled")  # Deshabilitar todos los botones

        mensaje = "Has perdido" if perdio else "Has ganado"  # Mensaje de fin del juego
        self.mostrar_mensaje(mensaje, "Fin del juego")  # Mostrar el mensaje de fin del juego

    # Mostrar un mensaje en una ventana emergente
    def mostrar_mensaje(self, mensaje, titulo):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        tk.Label(ventana, text=mensaje).pack()
        tk.Button(ventana, text="OK", command=ventana.destroy).pack()

# Crear la ventana principal y ejecutar el juego
if __name__ == "__main__":
    root = tk.Tk()
    app = Buscaminas(root)
    root.mainloop()