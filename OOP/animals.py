class Animals:
    def make_sound(self):
        pass
    def move(self):
        pass
    def eat(self):
        pass

class Bird(Animals):
    def make_sound(self):
        print("chirp")
    def eat(self):
        print("Chewing")
    def move(self):
        print("The bird is flying")

class fish(Animals):
    def make_sound(self):
        print("click")
    def eat(self):
        print("Grind")
    def move(self):
        print("Swimming")

class Dog(Animals):
    def make_sound(self):
        print("Berking")
    def eat(self):
        print("bite")
    def move(self):
        print("The dog is running")
