# keyboard arguments = arguements preceded by an identifier when we pass them to a function
#                     the order of the arguments doesn't matter, unlike posistional arguemts
#                     python knows the name of the arguments that our function receives


def hello(firstname, middlename, lastname):
    print("Hello " + firstname +  " " + middlename +  " " + lastname )


hello(lastname = "changcoco", middlename = "SKyclark", firstname = "Megel")
