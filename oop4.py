# Inheritance
class BIRD:
    def __init__(self, species):
        self.species = species
    
    def fly(self):
        return f"{self.species} is flying"

class PARROT(BIRD):
    def __init__(self, species, color):
        super().__init__(species)
        self.color = color

parrot = PARROT("Parrot", "Blue")
print(parrot.fly())
