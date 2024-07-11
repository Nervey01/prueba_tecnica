import tkinter as tk
from tkinter import messagebox
import random

# Función para tirar un dado
def tirar_dado():
    return random.randint(1, 6)

# Función para mostrar el dibujo de un dado en un label
def mostrar_dado(numero, label):
    if numero == 1:
        label.config(text="-------\n|     |\n|  *  |\n|     |\n-------")
    elif numero == 2:
        label.config(text="-------\n|*    |\n|     |\n|    *|\n-------")
    elif numero == 3:
        label.config(text="-------\n|*    |\n|  *  |\n|    *|\n-------")
    elif numero == 4:
        label.config(text="-------\n|*   *|\n|     |\n|*   *|\n-------")
    elif numero == 5:
        label.config(text="-------\n|*   *|\n|  *  |\n|*   *|\n-------")
    elif numero == 6:
        label.config(text="-------\n|*   *|\n|*   *|\n|*   *|\n-------")

# Función para lanzar los dados
def lanzar_dados():
    try:
        cantidad = int(entry.get())
        if cantidad < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido de dados.")
        return
    
    for widget in frame_dados.winfo_children():
        widget.destroy()
    
    for _ in range(cantidad):
        resultado = tirar_dado()
        label = tk.Label(frame_dados, font=("Courier", 14))
        label.pack(side=tk.LEFT, padx=10)
        mostrar_dado(resultado, label)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lanzador de Dados")

# Crear la entrada y el botón
entry = tk.Entry(ventana)
entry.pack(pady=10)
entry.insert(0, "2")  # Valor predeterminado

boton = tk.Button(ventana, text="Lanzar Dados", command=lanzar_dados)
boton.pack(pady=10)

# Frame para mostrar los resultados de los dados
frame_dados = tk.Frame(ventana)
frame_dados.pack(pady=10)

# Ejecutar la ventana principal
ventana.mainloop()
