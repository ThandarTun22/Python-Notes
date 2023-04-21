
class Animal:
    def __init__(self, name, food, legs) :
        self.name = name
        self.food = food
        self.legs = legs
        self._type = "Type is : "   # protected

    def display(self):
        print("Animal name is :", self.name)
        print(self.name," eat ", self.food)
        print(self.name, " have ", self.legs, "legs")
 
class Mammals(Animal):
    def __init__(self, name, food, legs, type):
        Animal.__init__(self, name, food, legs)
        self.type = type

    def getType(self):
        return self.type

class Birds(Animal):
    def __init__(self, name, food, legs, type):
        Animal.__init__(self, name, food, legs)
        self.type = type

    def getType(self):
        return self.type

class Fish(Animal):
    def __init__(self, name, food, legs, type):
        Animal.__init__(self, name, food, legs)
        self.type = type

    def getType(self):
        return self.type

class Reptiles(Animal):
    def __init__(self, name, food, legs, type):
        Animal.__init__(self, name, food, legs)
        self.type = type

    def getType(self):
        return self.type

class Amphibians(Animal):
    def __init__(self, name, food, legs, type):
        Animal.__init__(self, name, food, legs)
        self.type = type

    def getType(self):
        return self.type

# animal = Animal("dog")
# animal.display()

mammals = Mammals("dog", "snack", 4, "mammals")
mammals.display()
print(mammals._type,mammals.getType())

birds = Birds("birds", "snack", 2, "Birds")
birds.display()
print(birds._type,birds.getType())

fish = Fish("fish", "worm", "no", "Fish")
fish.display()
print(fish._type,fish.getType())
