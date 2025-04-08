import math


class FiguraGeometrica:
    def area(self):
        raise NotImplementedError("O método 'area' deve ser implementado.")

    def perimetro(self):
        raise NotImplementedError("O método 'perimetro' deve ser implementado.")


class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio

class Quadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

if __name__ == "__main__":
    figuras = [
        Circulo(5),     
        Quadrado(4),      
        Triangulo(2, 4, 2, 4, 6)  
    ]
    
    for figura in figuras:
        print(f"Figura: {figura.__class__.__name__}")
        print(f"Área: {figura.area():.2f}")
        print(f"Perímetro: {figura.perimetro():.2f}")
        print("-" * 30)
