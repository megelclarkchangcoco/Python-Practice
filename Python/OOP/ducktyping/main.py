# Duck typing = another way to achieve plymorphism besides Inheritance
#               Object must have the minimum necessary attributes/methods
#               If it look like a duck and squacks like a duck, it must be a duck.
from tkinter.ttk import Label  # Importing the Label class from the tkinter.ttk module

class Animal:
    alive = True  # Class attribute indicating that animals are alive

class Dog(Animal):  # Dog class inheriting from Animal
    def speak(self):  # Method to make the dog speak
        print("WOOF!")  # Print "WOOF!" when the dog speaks

class Cat(Animal):  # Cat class inheriting from Animal
    def speak(self):  # Method to make the cat speak
        print("MEOW!")  # Print "MEOW!" when the cat speaks

class Car:  # Car class, not inheriting from Animal
    alive = False  # Class attribute indicating that cars are not alive

    def speak(self):  # Method to make the car speak
        print("HONK!")  # Print "HONK!" when the car speaks

# List of different objects: Dog, Cat, and Car
animals = [Dog(), Cat(), Car()]

# Iterate through each object in the animals list
for animal in animals:
    animal.speak()  # Call the speak method of the current object
    print(animal.alive)  # Print the alive attribute of the current object
