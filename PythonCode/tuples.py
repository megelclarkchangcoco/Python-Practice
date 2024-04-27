# tuple = collection which is ordered and unchangeable
#           used to group together related data


student = ("megel", 21, "male")

print(student.count("Bro"))  # count where bro if no bro in list the value is zero
print(student.index("male")) # index of male is 2


for x in student:
    print(x) # print all element in student

if "bro" in student:
    print("bro is here!")  # if bro is here this is the out put
else:
    print("bro is not here!") # if bro is not in if statement condition the out will be this
