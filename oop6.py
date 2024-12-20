# Abstraction / ABC 

from abc import ABC

class ANIMAL(ABC):
    def make_sound(self):
        pass
    def make_move(self):
        pass
    def eat_food(self):
        return "eating meal!"
    
    
class LION(ANIMAL):
    def make_sound(self):
        return "ROAR!"
    def eat_food(self):
        return super().eat_food()

class DOG(ANIMAL):
    def make_sound(self):
        return "BARK!"
    def make_move(self):
        return "DANCE!"
    
lion = LION()
print(lion.make_sound())
print(lion.eat_food())

dog = DOG()
print(dog.make_sound())
print(dog.make_move())

dog = ANIMAL()
print(dog.make_sound())
