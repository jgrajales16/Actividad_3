import tkinter as tk

# Función para calcular el salario bruto y el salario neto
def calcular_salario():
    # Leer datos de entrada
    codigo_empleado = entry_codigo.get()
    nombres = entry_nombres.get()
    horas_trabajadas = int(entry_horas_trabajadas.get())
    valor_hora = float(entry_valor_hora.get())
    porcentaje_retencion = float(entry_porcentaje_retencion.get()) / 100  # Convertir el porcentaje a decimal
    
    # Calcular el salario bruto
    salario_bruto = horas_trabajadas * valor_hora
    
    # Calcular el salario neto
    salario_neto = salario_bruto * (1 - porcentaje_retencion)
    
    # Mostrar resultados
    resultado.config(text=f"Código del empleado: {codigo_empleado}\nNombres: {nombres}\nSalario Bruto: ${salario_bruto}\nSalario Neto: ${salario_neto}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Salario")

# Crear y colocar los widgets
tk.Label(ventana, text="Código del empleado:").pack()
entry_codigo = tk.Entry(ventana)
entry_codigo.pack()

tk.Label(ventana, text="Nombres:").pack()
entry_nombres = tk.Entry(ventana)
entry_nombres.pack()

tk.Label(ventana, text="Número de horas trabajadas al mes:").pack()
entry_horas_trabajadas = tk.Entry(ventana)
entry_horas_trabajadas.pack()

tk.Label(ventana, text="Valor hora trabajada:").pack()
entry_valor_hora = tk.Entry(ventana)
entry_valor_hora.pack()

tk.Label(ventana, text="Porcentaje de retención en la fuente:").pack()
entry_porcentaje_retencion = tk.Entry(ventana)
entry_porcentaje_retencion.pack()

# Mostrar mensaje sobre cómo ingresar el porcentaje de retención
tk.Label(ventana, text="Nota: El porcentaje de retención debe ingresarse como un número decimal. Por ejemplo, para un 10% de retención, ingrese '10'.").pack()

tk.Button(ventana, text="Calcular Salario", command=calcular_salario).pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
