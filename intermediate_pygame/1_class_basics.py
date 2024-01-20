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

#Create two dog objects
        
dog_1 = Dog('Thor', 'male', 8)
dog_2 = Dog('Nala', 'female', 2)

#Access attributes of each individual object

print(dog_1.name)
print(dog_2.gender)

dog_1.name = "Thooooorzin"
print(dog_1.name)
print()

dog_1.eat()
dog_2.eat()
print()

dog_1.bark(is_loud = False)
dog_2.bark(is_loud = True)
print()

dog_1.compute_age()
dog_2.compute_age()