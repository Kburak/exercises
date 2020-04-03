class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("WOOF!")

    #overrited the general
    def eat(self):
        print("I am a dog and eating")


mydog = Dog()

mydog.eat()

mydog.who_am_i()







