# membership operator = used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in

word = "Apple"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")


students = {"Spongbob", "Patrick", "Sandy"}

student= input("Enter the name of a student: ")

if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")


grades = {"Sandy":"A","Spongebob":"C","Patrick":"D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")


email = "megelnu@gmail.com"

if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid email")