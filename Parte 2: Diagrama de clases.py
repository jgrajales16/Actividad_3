from graphviz import Digraph

# Crear el diagrama de clases
dot = Digraph("Diagrama de Clases", format="png")
dot.attr(rankdir="TB", size="8,10")

# Ajustar los estilos generales de los nodos
node_attrs = {
    "shape": "record",
    "height": "1.2",
    "width": "1.5",
    "fontsize": "18",
    "fontname": "Arial"
}
dot.attr("node", **node_attrs)

# Clase base
dot.node("Figura", """{
    Figura |
    + nombre: str \\l
    + calcular_area(): float \\l
    + calcular_perimetro(): float \\l
}""")

# Clases derivadas
dot.node("Circulo", """{
    Circulo |
    + radio: int \\l
    + calcular_area(): float \\l
    + calcular_perimetro(): float \\l
}""")
dot.node("Cuadrado", """{
    Cuadrado |
    + lado: int \\l
    + calcular_area(): float \\l
    + calcular_perimetro(): float \\l
}""")
dot.node("Rectangulo", """{
    Rectangulo |
    + base: int \\l
    + altura: int \\l
    + calcular_area(): float \\l
    + calcular_perimetro(): float \\l
}""")
dot.node("TrianguloRectangulo", """{
    TrianguloRectangulo |
    + base: int \\l
    + altura: int \\l
    + calcular_area(): float \\l
    + calcular_perimetro(): float \\l
    + calcular_hipotenusa(): float \\l
    + determinar_tipo(): str \\l
}""")

# Relación de herencia
dot.edge("Figura", "Circulo")
dot.edge("Figura", "Cuadrado")
dot.edge("Figura", "Rectangulo")
dot.edge("Figura", "TrianguloRectangulo")

# Guardar y mostrar
diagram_path = "/mnt/data/Diagrama_de_Clases_Recreado"
dot.render(diagram_path, cleanup=True)

f"{diagram_path}.png"
