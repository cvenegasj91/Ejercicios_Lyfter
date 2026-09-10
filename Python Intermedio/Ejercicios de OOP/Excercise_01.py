class Circle():
    radius = 10
    def get_area(self, radius):
        self.area = (3.14 * radius * radius)
        return self.area
    

circle1 = Circle()
print(circle1.get_area(circle1.radius))