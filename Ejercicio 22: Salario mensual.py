
import tkinter as tk

# Función para calcular el salario mensual
def calcular_salario():
    # Leer datos de entrada
    nombre = entry_nombre.get()
    salario_hora = float(entry_salario_hora.get())
    horas_trabajadas = int(entry_horas_trabajadas.get())
    
    # Calcular el salario mensual
    salario_mensual = salario_hora * horas_trabajadas
    
    # Mostrar resultados
    if salario_mensual > 450000:
        resultado.config(text=f"Nombre: {nombre}\nSalario Mensual: ${salario_mensual}")
    else:
        resultado.config(text=f"Nombre: {nombre}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Salario Mensual")

# Crear y colocar los widgets
tk.Label(ventana, text="Nombre del empleado:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Salario básico por hora:").pack()
entry_salario_hora = tk.Entry(ventana)
entry_salario_hora.pack()

tk.Label(ventana, text="Número de horas trabajadas en el mes:").pack()
entry_horas_trabajadas = tk.Entry(ventana)
entry_horas_trabajadas.pack()

tk.Button(ventana, text="Calcular Salario", command=calcular_salario).pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
