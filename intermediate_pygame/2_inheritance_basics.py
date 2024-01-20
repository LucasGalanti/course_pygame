class Dog():
    """ A class to represent a general dog"""

    def __init__(self, dog_name, dog_gender, dog_age):
        """Initialize attributes"""
        self.name = dog_name
        self.gender = dog_gender
        self.age = dog_age

    def eat(self):
        """Feed the dog"""
        if self.gender == "male":
            print('Here ' + self.name + "! Good Boy! Eat Up")
        if self.gender == "female":
            print('Here ' + self.name + "! Good Girl! Eat Up")

    def bark(self, is_loud = True):
        """Get the dog to speak"""
        if is_loud:
            print("WOOF WOOF WOOF")
        else:
            print('woof...')

    def compute_age(self):
        """Compute the age in dog years"""
        dog_years = self.age*7
        print(self.name + " is " + str(dog_years) + " years old")

class Beagle(Dog): #this indicate Dog is a superclass for Beagle
    """ A class to represent a specifc type of dog """

    def __init__(self, dog_name, dog_gender, dog_age, coward_dog = True):
        #Call the initialization of the super(parent) class
        super().__init__(dog_name, dog_gender, dog_age)
        self.is_gun_shy = coward_dog
    
    def hunt(self):
        """If the dog is not gun shy, take them hunting"""
        if not self.is_gun_shy:
            self.bark()
            print(self.name + " just brought back a duck")
        else:
            print(self.name + " is not a good hunting dog.")

    def bark(self):
        """get the dog to speak, rewrinting the super parent method"""
        print("HOOOOOOWWWWWWL")

dog_1 = Beagle('Thor', 'male', 8, coward_dog = False)
#dog_1 will have both the attributes and methods for the class Dog and the class Beagle

dog_1.eat()
dog_1.compute_age()

dog_1.hunt()

dog_2 = Beagle('Nala', 'female', 10, coward_dog = True)

dog_2.hunt()

dog_3 = Dog('Doggie', 'male', 12)

dog_3.bark()

dog_2.bark()