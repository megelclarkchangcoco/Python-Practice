
# Variable  = a container for a value. behaves as the value that it contains.

firstname = "Miguel" # String type
lastname = "Changcoco" # String type
Age = 21  # int type
height = 165.0 # Float type
human = True # Boolean

fullname = firstname + " " + lastname

print("Your Name is " + fullname)
print(type(fullname))

print("I'm ", Age)
print(type(Age))

print("Your Height is ", height)
print(type(height))

print("Is this human " + str(human))
print(type(human))

# multiple assignment = allow us to assign multiple variable at the same time in one line of code
fname, lname, ages, attractive = "Miguel", "Changcoco", 21, True

print(fname)
print(lname)
print(ages)
print(attractive)


one = two = three = four = five = 6
print(one)
