import tkinter as tk
import math

# Definición de la función para calcular el perímetro, la altura y el área de un triángulo equilátero
def calcular_triangulo_equilatero():
    # Valor del lado del triángulo equilátero
    lado = float(entry_lado.get())
    
    # Cálculo del perímetro
    perimetro = 3 * lado
    
    # Cálculo de la altura
    altura = (math.sqrt(3) / 2) * lado
    
    # Cálculo del área
    area = (math.sqrt(3) / 4) * (lado ** 2)
    
    # Mostrar los resultados
    resultado_perimetro.config(text=f"Perímetro: {perimetro}")
    resultado_altura.config(text=f"Altura: {altura}")
    resultado_area.config(text=f"Área: {area}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Triángulo Equilátero")

# Crear y colocar los widgets
tk.Label(ventana, text="Lado del triángulo:").pack()
entry_lado = tk.Entry(ventana)
entry_lado.pack()

tk.Button(ventana, text="Calcular", command=calcular_triangulo_equilatero).pack()

resultado_perimetro = tk.Label(ventana, text="")
resultado_perimetro.pack()

resultado_altura = tk.Label(ventana, text="")
resultado_altura.pack()

resultado_area = tk.Label(ventana, text="")
resultado_area.pack()

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
