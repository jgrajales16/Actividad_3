import tkinter as tk
import math

# Función para calcular la raíz cuadrada, el cuadrado y el cubo de un número
def calcular():
    # Leer datos de entrada
    numeros = entry_numeros.get().split()
    resultados = []
    
    for num in numeros:
        num = int(num)
        raiz_cuadrada = math.sqrt(num)
        cuadrado = num ** 2
        cubo = num ** 3
        resultados.append(f"Número: {num}, Raíz Cuadrada: {raiz_cuadrada}, Cuadrado: {cuadrado}, Cubo: {cubo}")
    
    resultado.config(text="\n".join(resultados))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculos de Números Enteros Positivos")

# Crear y colocar los widgets
tk.Label(ventana, text="Ingrese números enteros positivos separados por espacios:").pack()
entry_numeros = tk.Entry(ventana)
entry_numeros.pack()

tk.Button(ventana, text="Calcular", command=calcular).pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
