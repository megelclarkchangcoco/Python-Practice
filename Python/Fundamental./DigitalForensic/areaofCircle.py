
import math
# function to solve circle radius
def areaofCircle():
    while(True):
        radius = int(input("Enter a Radius:"))

        values = math.pi*(radius * radius)
        print(values)

        ask = str(input("do you want try again?"))

        if(ask == 'no'):
            return False

# Input radius of Circle
areaofCircle()





