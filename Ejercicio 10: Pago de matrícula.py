import tkinter as tk

# Función para calcular el pago de matrícula
def calcular_pago():
    # Leer datos de entrada
    NI = entry_NI.get()
    NOM = entry_NOM.get()
    PAT = float(entry_PAT.get())
    ES = int(entry_ES.get())
    PAGMAT = 50000
    
    # Algoritmo
    if PAT > 2000000 and ES > 3:
        PAGMAT += 0.03 * PAT
    
    # Mostrar resultados
    resultado.config(text=f"EL ESTUDIANTE CON NUMERO DE INSCRIPCION {NI} Y NOMBRE {NOM} DEBE PAGAR: ${PAGMAT}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Pago de Matrícula")

# Crear y colocar los widgets
tk.Label(ventana, text="Número de inscripción:").pack()
entry_NI = tk.Entry(ventana)
entry_NI.pack()

tk.Label(ventana, text="Nombres:").pack()
entry_NOM = tk.Entry(ventana)
entry_NOM.pack()

tk.Label(ventana, text="Patrimonio:").pack()
entry_PAT = tk.Entry(ventana)
entry_PAT.pack()

tk.Label(ventana, text="Estrato social:").pack()
entry_ES = tk.Entry(ventana)
entry_ES.pack()

tk.Button(ventana, text="Calcular Pago", command=calcular_pago).pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
