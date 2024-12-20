# Another example on Class definition and objects instantiation

class CAR:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def start(self):
        return f"{self.brand} car with {self.color} color has started."
    
    
car1 = CAR("Toyota", "Red")
car2 = CAR("BMW", "Black")

print(car1.start())
print(car2.start())
