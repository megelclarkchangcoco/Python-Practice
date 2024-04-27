# scope = the region that a variable is recognized
#         a variable is only available from inside the region it is created
#         a global and locally scoped versions of a variable can be created


name = "Negel" # global scope (available inside & outside function)


def display():
    name = "changcoco" # local scope (available only inside this function)
    print(name)


print(name)
display()
