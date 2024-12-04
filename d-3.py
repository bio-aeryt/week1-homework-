import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        result = self.side**2
        return result

    def diagonal(self):
        result = round(math.sqrt(self.side**2 + self.side**2), 2)
        return result


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
