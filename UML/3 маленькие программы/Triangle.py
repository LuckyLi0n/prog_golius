class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Rectangle(Shape):
    def area(self):
        area = self.width*self.height
        return area


class Triangle(Shape):
    def area(self):
        area = self.width*self.height/2
        return area


t = Triangle(100, 40)
r = Rectangle(100, 40)

print(t.area())
print(r.area())
