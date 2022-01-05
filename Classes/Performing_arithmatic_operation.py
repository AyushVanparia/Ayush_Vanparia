class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # magic methods for performing arithmatic operation between two objects

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"X = {self.x}, Y = {self.y}"


point1 = Point(10, 20)
point2 = Point(1, 2)

print(point1 + point2)
