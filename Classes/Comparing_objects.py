class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # magic method for comparing two objects
    def __eq__(self, other):  # similar to "==" operator
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):  # similar to ">" operator
        return self.x > other.x and self.y > other.y


point1 = Point(10, 20)
point2 = Point(1, 2)
print(point1 > point2)
