import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = math.pi * self.radius**2
        return round(result, 2)

    def perimeter(self):
        result = math.pi * 2 * self.radius
        return round(result, 2)


# # 半径1の円
circle1 = Circle(radius=1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# # 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 18.85
