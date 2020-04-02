"""
Fill in the class
"""

class Cylinder():

    pi = 3.14

    def __init__(self,height=1, radius=1):

        self.height = height
        self.radius = radius


    def volume(self):
        return self.height * Cylinder.pi * ((self.radius)**2)

    def surface_area(self):
        return (2 * Cylinder.pi*((self.radius)**2)) + (2*Cylinder.pi*self.radius*self.height)


c = Cylinder(2,3)

print(c.volume())

print(c.surface_area())
