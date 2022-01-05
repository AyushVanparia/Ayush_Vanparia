class Animal:
    def eat(self):
        print("Eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    def walk(self):
        print("walk")


c = Chicken()
print(issubclass(Chicken, Animal))
