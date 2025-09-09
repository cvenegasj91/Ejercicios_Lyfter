from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius ** 2
        return area
    
    def calculate_perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        area = self.side ** 2
        return area
    
    def calculate_perimeter(self):
        perimeter = 4 * self.side
        return perimeter


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        return area
    
    def calculate_perimeter(self):
        perimeter = 2*(self.width + self.height)
        return perimeter
    


circle = Circle(30)
print(f'\nRadio del circulo: {circle.radius} cm')
print(f'Area: {circle.calculate_area()} cm')
print(f'Perimetro: {circle.calculate_perimeter()} cm')

square = Square(40)
print(f'\nLado del cuadrado: {square.side} cm')
print(f'Area: {square.calculate_area()} cm')
print(f'Perimetro: {square.calculate_perimeter()} cm')

rectangle = Rectangle(40, 75)
print(f'\nRectangulo: Base: {rectangle.width} cm Altura: {rectangle.height} cm')
print(f'Area: {rectangle.calculate_area()} cm')
print(f'Perimetro: {rectangle.calculate_perimeter()} cm')