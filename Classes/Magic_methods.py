class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # methods who has two underscore sign"_" before and after is called magic method

    def __str__(self):
        return f"({self.x},{self.y})"


point = Point(1, 2)
print(point)
