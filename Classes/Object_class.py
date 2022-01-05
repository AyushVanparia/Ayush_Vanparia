# object class is base class for all class in python

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
print(isinstance(m, object))
# issubclass() checks if a class is derived from another class
print(issubclass(Animal, object))
