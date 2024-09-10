
# Class methods = Allow operation related to the class itself
#                take (cls) as the first parameter, which represents the class itself.


class Student:

    count = 0
    total_gpa = 0

    def __init__(self,name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #Instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average of {cls.total_gpa / cls.count}.2f"
student1 = Student("Miguel", 3.2)
student2 = Student("Edicl", 3.2)
student3 = Student("Loiuse", 3.2)

print(Student.get_count())
print(Student.get_average_gpa())