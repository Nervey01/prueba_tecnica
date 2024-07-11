import tkinter as tk
import random

class DadoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Dado")

        self.canvas = tk.Canvas(root, width=200, height=200, bg="white")
        self.canvas.pack(pady=20)

        self.lanzar_button = tk.Button(root, text="Lanzar Dado", command=self.lanzar_dado, font=("Helvetica", 24))
        self.lanzar_button.pack(pady=20)

    def lanzar_dado(self):
        resultado = random.randint(1, 6)
        self.dibujar_dado(resultado)

    def dibujar_dado(self, numero):
        self.canvas.delete("all")
        if numero in (1, 3, 5):
            self.dibujar_punto(100, 100)
        if numero in (2, 3, 4, 5, 6):
            self.dibujar_punto(50, 50)
            self.dibujar_punto(150, 150)
        if numero in (4, 5, 6):
            self.dibujar_punto(150, 50)
            self.dibujar_punto(50, 150)
        if numero == 6:
            self.dibujar_punto(50, 100)
            self.dibujar_punto(150, 100)

    def dibujar_punto(self, x, y):
        radio = 15
        self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="Black")

if __name__ == "__main__":
    root = tk.Tk()
    app = DadoApp(root)
    root.mainloop()
