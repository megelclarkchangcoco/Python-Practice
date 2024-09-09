# Class variable = Shared among all instances of a class
#                  Defined outside the constructor
#                  Allows you to share data among all objects created from that class

class Student:

    # Class variables shared among all instances
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        # Instance variables unique to each instance
        self.name = name
        self.age = age
        # Increment the class variable for each new instance
        Student.num_students += 1

# Creating instances of the Student class
student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidwards", 55)
student4 = Student("Sandy", 27)

# Accessing instance variables and class variables
print(student1.name)       # Output: Spongebob
print(student1.age)        # Output: 30
print(student1.class_year) # Output: 2024 (shared class variable)

print(student2.name)       # Output: Patrick
print(student2.age)        # Output: 35
print(student2.class_year) # Output: 2024 (shared class variable)

# Accessing the class variable directly from the class
print(Student.num_students) # Output: 4

# Using an f-string to print a formatted message
print(f"My Graduating class of {Student.class_year} has {Student.num_students} students")
