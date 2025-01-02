import tkinter as tk

# Función para encontrar el mayor valor entre un grupo de datos positivos
def encontrar_mayor():
    # Leer datos de entrada
    numeros = entry_numeros.get().split()
    numeros = [int(num) for num in numeros if int(num) > 0]
    
    if numeros:
        mayor_valor = max(numeros)
        resultado.config(text=f"El mayor valor es: {mayor_valor}")
    else:
        resultado.config(text="No se ingresaron números positivos")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Encontrar el Mayor Valor")

# Crear y colocar los widgets
tk.Label(ventana, text="Ingrese números positivos separados por espacios:").pack()
entry_numeros = tk.Entry(ventana)
entry_numeros.pack()

tk.Button(ventana, text="Encontrar Mayor", command=encontrar_mayor).pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
