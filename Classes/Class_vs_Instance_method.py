class Point:
    # class attribute
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod  # decorator
    # class method
    def Zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point({self.x}, {self.y})")


point = Point.Zero()
point.draw()
