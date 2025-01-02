import tkinter as tk
import math

# Función para calcular las soluciones de la ecuación de segundo grado
def calcular_soluciones():
    # Leer datos de entrada
    A = float(entry_A.get())
    B = float(entry_B.get())
    C = float(entry_C.get())
    
    # Calcular el discriminante
    discriminante = B**2 - 4*A*C
    
    # Determinar las soluciones
    if discriminante > 0:
        sol1 = (-B + math.sqrt(discriminante)) / (2*A)
        sol2 = (-B - math.sqrt(discriminante)) / (2*A)
        resultado.config(text=f"Soluciones: {sol1} y {sol2}")
    elif discriminante == 0:
        sol = -B / (2*A)
        resultado.config(text=f"Solución única: {sol}")
    else:
        resultado.config(text="No hay soluciones reales")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Soluciones de la Ecuación de Segundo Grado")

# Crear y colocar los widgets
tk.Label(ventana, text="Valor de A:").pack()
entry_A = tk.Entry(ventana)
entry_A.pack()

tk.Label(ventana, text="Valor de B:").pack()
entry_B = tk.Entry(ventana)
entry_B.pack()

tk.Label(ventana, text="Valor de C:").pack()
entry_C = tk.Entry(ventana)
entry_C.pack()

tk.Button(ventana, text="Calcular Soluciones", command=calcular_soluciones).pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
