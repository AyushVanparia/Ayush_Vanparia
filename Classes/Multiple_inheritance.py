class Flyer:
    def fly(self):
        print("fly")


class Swimer:
    def swim(self):
        print("swim")


class FlyingFish(Flyer, Swimer):
    def process(self):
        print("It does both")


ff = FlyingFish()
ff.fly()
ff.swim()
