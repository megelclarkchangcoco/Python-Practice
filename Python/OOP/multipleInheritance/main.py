# Multiple inheritance: Inherit from more than one parent class
#                        C(A, B)

# Multilevel inheritance: Inherit from a parent which inherits from another parent
#                           C(B) <- B(A) <- A

class Animal:
    # Constructor method to initialize the name attribute
    def __init__(self, name):
        self.name = name

    # Method to simulate the animal eating
    def eat(self):
        print(f"{self.name} is eating")

    # Method to simulate the animal sleeping
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    # Method to simulate the prey fleeing
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    # Method to simulate the predator hunting
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    # Inherits from both Animal and Prey classes
    pass

class Hawk(Predator):
    # Inherits from Predator class, which in turn inherits from Animal
    pass

class Fish(Predator, Prey):
    # Inherits from Predator and Prey classes, which in turn inherit from Animal
    pass

# Creating an instance of Rabbit with the name "Bugs"
rabbit = Rabbit("Bugs")
# Creating an instance of Hawk with the name "Tony"
hawk = Hawk("Tony")
# Creating an instance of Fish with the name "Nemo"
fish = Fish("Nemo")

# Calling the flee method on the rabbit instance
rabbit.flee()  # Bugs is fleeing
# Calling the sleep method on the hawk instance
hawk.sleep()   # Tony is sleeping
# Calling the eat method on the fish instance
fish.eat()     # Nemo is eating
