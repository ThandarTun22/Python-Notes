
class Polygons:
    def __init__(self, name, sides, vertices, diagonals, sum_angles) :
        self.name = name
        self.sides = sides
        self.vertices = vertices
        self.diagonals = diagonals
        self.sum_angles = sum_angles

    def display(self):
        print(self.name)
        print(f". Has {self.sides} sides and {self.vertices} vertices")
        print(f". Has {self.diagonals} diagonals")
        print(f". Sum of the interior angles is {self.sum_angles}")

class Triangle(Polygons):
    def __init__(self, name, sides, vertices, diagonals, sum_angles):
        Polygons.__init__(self, name, sides, vertices, diagonals, sum_angles)
        self.name = name
        self.sides = sides
        self.vertices = vertices
        self.diagonals = diagonals
        self.sum_angles = sum_angles

class Quadrilateral(Polygons):
    def __init__(self, name, sides, vertices, diagonals, sum_angles):
        Polygons.__init__(self, name, sides, vertices, diagonals, sum_angles)
        self.name = name
        self.sides = sides
        self.vertices = vertices
        self.diagonals = diagonals
        self.sum_angles = sum_angles

class Pentagon(Polygons):
    def __init__(self, name, sides, vertices, diagonals, sum_angles):
        Polygons.__init__(self, name, sides, vertices, diagonals, sum_angles)
        self.name = name
        self.sides = sides
        self.vertices = vertices
        self.diagonals = diagonals
        self.sum_angles = sum_angles

class Hexagon(Polygons):
    def __init__(self, name, sides, vertices, diagonals, sum_angles):
        Polygons.__init__(self, name, sides, vertices, diagonals, sum_angles)
        self.name = name
        self.sides = sides
        self.vertices = vertices
        self.diagonals = diagonals
        self.sum_angles = sum_angles

polygons = Polygons("Triangle", 3, 3, "no", "180 degree" )
polygons.display()

triangle = Triangle("Triangle", 3, 3, "no", "180 degree")
triangle.display()

quadrilateral = Quadrilateral("Quadrilateral", 4, 4, "two", "360 degree")
quadrilateral.display()

pentagon = Pentagon("Pentagon", 5, 5, "5", "540 degree")
pentagon.display()

hexagon = Hexagon("Hexagon", 6, 6, "9", "720 degree")
hexagon.display()