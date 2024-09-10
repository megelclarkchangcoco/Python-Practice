# Static methods = A method that belong to a class raather tahn any object from that class (Instance)
#                  Usually used for general utility function
#

# Instance method = Best for operation on instances of the class (Object)
# Static methods = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name  # Initialize the name attribute
        self.position = position  # Initialize the position attribute

    def get_info(self):
        # Return a string containing the employee's name and position
        return f"{self.name} = {self.position}"

    #staticmethod
    def is_valid_position(position):
        # List of valid positions
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        # Check if the given position is in the list of valid positions
        return position in valid_positions

# Create instances of Employee with different names and positions
employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Squaidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

# Check if "Cook" is a valid position and print the result
print(Employee.is_valid_position("Cook"))
# Print the information of each employee
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())







