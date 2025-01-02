import math
import tkinter as tk
from tkinter import messagebox

# Clase base para todas las figuras geométricas
class Figura:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la figura

    def calcular_area(self):
        pass  # Este método lo implementarán las clases hijas

    def calcular_perimetro(self):
        pass  # Este también lo implementarán las hijas

# Clase para círculos
class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio  # Atributo que guarda el radio del círculo

    def calcular_area(self):
        return math.pi * self.radio ** 2  # Fórmula del área: pi * r^2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio  # Fórmula del perímetro: 2pir

# Clase para rectángulos
class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base  # Base del rectángulo
        self.altura = altura  # Altura del rectángulo

    def calcular_area(self):
        return self.base * self.altura  # Fórmula del área: base * altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)  # Fórmula del perímetro

# Clase para cuadrados
class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado  # Lado del cuadrado

    def calcular_area(self):
        return self.lado ** 2  # Área: lado^2

    def calcular_perimetro(self):
        return 4 * self.lado  # Perímetro: 4 * lado

# Clase para triángulos rectángulos
class TrianguloRectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Triángulo Rectángulo")
        self.base = base  # Base del triángulo
        self.altura = altura  # Altura del triángulo

    def calcular_area(self):
        return (self.base * self.altura) / 2  # Área: (base * altura) / 2

    def calcular_perimetro(self):
        hipotenusa = self.calcular_hipotenusa()  # Llamar al método de hipotenusa
        return self.base + self.altura + hipotenusa

    def calcular_hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)  # Teorema de Pitágoras

    def determinar_tipo(self):
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura == hipotenusa:
            return "Equilátero"  # Todos los lados son iguales
        elif self.base != self.altura != hipotenusa:
            return "Escaleno"  # Todos los lados son diferentes
        else:
            return "Isósceles"  # Dos lados son iguales

# Clase para la interfaz gráfica
class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Figuras Geométricas")

        # Selección de figura
        self.label_figura = tk.Label(root, text="Seleccione la figura:")
        self.label_figura.pack()

        self.figura_var = tk.StringVar(value="Círculo")
        self.figura_var.trace("w", self.actualizar_parametros)
        tk.Radiobutton(root, text="Círculo", variable=self.figura_var, value="Círculo").pack()
        tk.Radiobutton(root, text="Rectángulo", variable=self.figura_var, value="Rectángulo").pack()
        tk.Radiobutton(root, text="Cuadrado", variable=self.figura_var, value="Cuadrado").pack()
        tk.Radiobutton(root, text="Triángulo Rectángulo", variable=self.figura_var, value="Triángulo Rectángulo").pack()

        # Entradas de parámetros
        self.label_param1 = tk.Label(root, text="Parámetro 1:")
        self.label_param1.pack()
        self.entry_param1 = tk.Entry(root)
        self.entry_param1.pack()

        self.label_param2 = tk.Label(root, text="Parámetro 2:")
        self.label_param2.pack()
        self.entry_param2 = tk.Entry(root)
        self.entry_param2.pack()

        # Botón para calcular
        self.boton_calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.boton_calcular.pack()

        # Resultados
        self.resultado_area = tk.Label(root, text="Área:")
        self.resultado_area.pack()
        self.resultado_perimetro = tk.Label(root, text="Perímetro:")
        self.resultado_perimetro.pack()
        self.resultado_tipo = tk.Label(root, text="")
        self.resultado_tipo.pack()

        self.actualizar_parametros()

    def actualizar_parametros(self, *args):
        figura = self.figura_var.get()
        if figura in ["Círculo", "Cuadrado"]:
            self.label_param2.pack_forget()
            self.entry_param2.pack_forget()
            self.label_param1.config(text="Parámetro 1 (radio/lado):")
        else:
            self.label_param2.pack()
            self.entry_param2.pack()
            self.label_param1.config(text="Parámetro 1 (base):")
            self.label_param2.config(text="Parámetro 2 (altura):")

    def calcular(self):
        figura = self.figura_var.get()
        try:
            param1 = float(self.entry_param1.get())
            param2 = self.entry_param2.get()
            param2 = float(param2) if param2 else None

            if figura == "Círculo":
                circulo = Circulo(param1)
                area = circulo.calcular_area()
                perimetro = circulo.calcular_perimetro()
                self.resultado_tipo.config(text="")
            elif figura == "Rectángulo":
                if param2 is None:
                    raise ValueError("El rectángulo necesita dos parámetros.")
                rectangulo = Rectangulo(param1, param2)
                area = rectangulo.calcular_area()
                perimetro = rectangulo.calcular_perimetro()
                self.resultado_tipo.config(text="")
            elif figura == "Cuadrado":
                cuadrado = Cuadrado(param1)
                area = cuadrado.calcular_area()
                perimetro = cuadrado.calcular_perimetro()
                self.resultado_tipo.config(text="")
            elif figura == "Triángulo Rectángulo":
                if param2 is None:
                    raise ValueError("El triángulo necesita dos parámetros.")
                triangulo = TrianguloRectangulo(param1, param2)
                area = triangulo.calcular_area()
                perimetro = triangulo.calcular_perimetro()
                tipo = triangulo.determinar_tipo()
                self.resultado_tipo.config(text=f"Tipo: {tipo}")

            self.resultado_area.config(text=f"Área: {area:.2f}")
            self.resultado_perimetro.config(text=f"Perímetro: {perimetro:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

# Inicializar la aplicación
def main():
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()

if __name__ == "__main__":
    main()
