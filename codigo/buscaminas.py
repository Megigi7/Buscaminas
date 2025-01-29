import tkinter as tk
from tkinter import ttk





def cambiar_dificultad(event):
    dificultad = event.widget.get()
    print(dificultad)

def crear_ventana_buscaminas():
    # Creacion de la ventana y peronalización
    ventana = tk.Tk()
    ventana.title("Buscaminas")
    ventana.geometry("600x400")
    ventana.iconbitmap("img/icono.ico")
    ventana.minsize(600, 400)
    ventana.maxsize(600, 400)

    # Encabezado
    encabezado = tk.Frame(ventana, relief=tk.RAISED, borderwidth=2)
    encabezado.pack(side=tk.TOP, fill=tk.X)

    # Título del juego
    titulo = tk.Label(encabezado, text="BUSCAMINAS", font=("Arial", 16), fg="darkgreen")
    titulo.pack(side=tk.LEFT, padx=10)

    # Selector de dificultad
    dificultad_label = tk.Label(encabezado, text="Dificultad", font=("Arial", 10))
    dificultad_label.pack(side=tk.LEFT, padx=10)

    dificultad_selector = ttk.Combobox(encabezado, values=["Principiante", "Intermedio", "Experto"], state="readonly")
    dificultad_selector.set("Principiante")
    dificultad_selector.pack(side=tk.LEFT)
    dificultad_selector.bind("<<ComboboxSelected>>", cambiar_dificultad)

    # Contador de minas restantes
    minas_frame = tk.Frame(encabezado)
    minas_frame.pack(side=tk.LEFT, padx=20)

    bandera_icono = tk.Label(minas_frame, text="\u2691", font=("Arial", 16), fg="red")  # Icono de bandera
    bandera_icono.pack(side=tk.LEFT)

    minas_restantes = tk.Label(minas_frame, text="99", font=("Arial", 14)) # VALOR VARIA SEGUN DIFICUKTAD Y DISMINUYE AL PONER UNA BANDERA
    minas_restantes.pack(side=tk.LEFT, padx=5)

    # Temporizador
    temporizador = tk.Label(encabezado, text="00:00", font=("Arial", 14), relief=tk.SUNKEN, width=6) #TEMPORIZADOR QUE SUMA VALOR CADA SEGUNDO
    temporizador.pack(side=tk.RIGHT, padx=20)

    # Puntajes
    puntajes_frame = tk.Frame(ventana, relief=tk.SUNKEN, borderwidth=2)
    puntajes_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

    record_label = tk.Label(puntajes_frame, text="RECORD:", font=("Arial", 12)) #DEBE HABER UN RECORD POR CADA DIFICULTAD
    record_label.pack(pady=5)

    record_puntos = tk.Label(puntajes_frame, text="", font=("Arial", 12), relief=tk.SUNKEN, width=12)
    record_puntos.pack(pady=5)

    # Tablero de cuadrículas
    tablero_frame = tk.Frame(ventana, relief=tk.SUNKEN, borderwidth=2)
    tablero_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Botones de la cuadrícula

    ventana.mainloop()


crear_ventana_buscaminas()