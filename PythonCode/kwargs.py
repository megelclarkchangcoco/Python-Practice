# **kwargs = parameter that will pack all argumetns into a dictionary
#           useful so that a function can accept a varying amount of keyboard argumentss

def fullname(**kwargs):
    #print("Hello "+ kwargs['First'] + " " + kwargs['Middle'] + " " + kwargs['last'])
    print("Hello ", end = " ")
    for key, value in kwargs.items():
        print(value, end = " ")


fullname(First = "Megel", Middle="Christian", last="Polison")
