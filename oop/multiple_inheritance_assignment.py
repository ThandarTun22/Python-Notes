
class Sides:
    def __init__(self, sides) :
        self.sides = sides

class Vertices:
    def __init__(self, vertices) :
        self.vertices = vertices

class Diagonals:
    def __init__(self, diagonals):
        self.diagonals = diagonals

class SumOfAngles:
    def __init__(self, sum_of_angles):
        self.sum_of_angles = sum_of_angles

class Triangle(Sides, Vertices, Diagonals, SumOfAngles):
    def __init__(self,name, sides, vertices, diagonals, sum_of_angles):
        Sides.__init__(self, sides)
        Vertices.__init__(self, vertices)
        Diagonals.__init__(self, diagonals)
        SumOfAngles.__init__(self, sum_of_angles)
        self.name = name

    def info(self):
        print(self.name)
        print(f". Has {self.sides} sides and {self.vertices} vertices")
        print(f". Has {self.diagonals} diagonals")
        print(f". Sum of the interior angles is {self.sum_of_angles}")

triangle = Triangle("Triangle", 3, 3, "no", "180 degree" )
triangle.info()

quadrilateral = Triangle("Quadrilateral", 4, 4, "two", "360 degree")
quadrilateral.info()

pentagon = Triangle("Pentagon", 5, 5, "5", "540 degree")
pentagon.info()

hexagon = Triangle("Hexagon", 6, 6, "9", "720 degree")
hexagon.info()

heptagon = Triangle("Heptagon", 7, 7, "14", "900 degree")
heptagon.info()

octagon = Triangle("Octagon", 8, 8, "20", "1080 degree" )
octagon.info()

nonagon = Triangle("Nonagon", 9, 9, "27", "1260 degree")
nonagon.info()

decagon = Triangle("Decagon", 10, 10, "35", "1440 degree")
decagon.info()
