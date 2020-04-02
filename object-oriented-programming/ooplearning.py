class Dog():
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = "mammal"

    def __init__(self, breed, name):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name

    # OPERATIONS/Actions --> Methods
    def bark(self,number):
        print("WOOF! My name is {} and the number is {}".format(self.name,number))


my_dog = Dog(breed="Lab", name="Ceku")

print(type(my_dog))
print(my_dog.species)
print(my_dog.name)
print(my_dog.breed)

print(my_dog.bark(10))








class Circle():

    #CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius=1):

        self.radius = radius
        self.area = radius * radius *Circle.pi

    # METHOD
    def get_circumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)