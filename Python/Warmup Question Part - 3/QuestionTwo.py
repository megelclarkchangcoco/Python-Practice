
# Question Two : Dictionary
# Write a Python program that takes a dictionary representing a student's grades (subject as key and grade as value) as input and calculates the average grade.
#
# Sample Input:
# {'Math': 85, 'Science': 90, 'English': 88}
#
# Sample Output:
# Average grade: 87.67



grade = {
         'Math': 85,
         'Science':90,
         'English': 88
         }

totalGrade = sum(grade.values())
numSub = len(grade)
avgGrade = totalGrade / numSub

print(avgGrade)

