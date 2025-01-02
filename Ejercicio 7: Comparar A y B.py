import tkinter as tk

# Función para comparar A y B
def comparar():
    # Definición de variables
    A = int(entry_A.get())
    B = int(entry_B.get())
    
    # Algoritmo
    if A > B:
        resultado.config(text="A ES MAYOR QUE B")
    elif A == B:
        resultado.config(text="A ES IGUAL A B")
    else:
        resultado.config(text="A ES MENOR QUE B")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Comparación de A y B")

# Crear y colocar los widgets
tk.Label(ventana, text="Valor de A:").pack()
entry_A = tk.Entry(ventana)
entry_A.pack()

tk.Label(ventana, text="Valor de B:").pack()
entry_B = tk.Entry(ventana)
entry_B.pack()

tk.Button(ventana, text="Comparar", command=comparar).pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
