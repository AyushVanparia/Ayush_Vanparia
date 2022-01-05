# defininf classes
class Point:
    def draw(self):
        print("draw")


# creating object of the class
point = Point()
print(type(point))

# isistance lets us check if the object is the instance of the specified class
print(isinstance(point, Point))
