# Object Oriented Programming in Python
# OOP is one of many paradigms in programming.
# A paradigm is an approach / style through which you can organize your code.

# Define a class
class DOG:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Wuuf!"
    
    def play(self):
        return f"{self.name} of {self.breed} breed can play with their friends!"

# Create an object
dog1 = DOG("Boozer", "Jack Russel")
print(dog1.bark())
print(dog1.play())

dog2 = DOG("Slurpy", "Golden Retriever")
print(dog2.bark())
print(dog2.play())

