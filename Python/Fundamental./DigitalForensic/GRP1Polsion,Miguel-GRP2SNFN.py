
import math
def rectangle():
    while (True):
        base = float(input("Enter the Base of Triangle:"))
        height = float(input("Enter the Height of Triangle:"))

        area = 0.5 * base * height  # computation of area

        print(area)  # print
        # ask again
        ask = input("do you want try again?  (yes or no):").lower()

        if (ask == "no"):
            start()
            return False
def circle():
    while (True):
        radius = float(input("Enter a Radius:"))

        values = math.pi * (radius * radius)
        print(values)

        ask = str(input("do you want try again? (yes or no):"))

        if (ask == 'no'):
            start()
            return False
def trapezoid():
    # while loop to repeatedly perform calculatiom
    while (True):
        baseOne = float(input("Enter a number of  base one :"))
        baseTwo = float(input("Enter a number of base two :"))
        height = float(input("Enter a number of Height : "))

        area = ((baseOne + baseTwo) / 2) * height
        print(f"base of trapezoid {area}")

        # ask if want calculate again
        ask = str(input("You want calculate again? (yes or no): ")).lower()
        if (ask == "no"):
            start()
            return False
def triangle():
    while(True):
        length = float(input("Enter number of length :"))
        width = float(input("Enter number of width :"))

        result = length * width
        print("Area of  Rectangle", str(result))

        ask = input("do you want calculate again? (yes or no )").lower()
        if( ask == "no"):
            start()
            return False


def start():
    while(True):
        print("Choose to Compute:")
        print("a) Area of a rectangle")
        print("b) Area of a circle")
        print("c) Area of a trapezoid")
        print("d) Area of a triangle")
        choose = input("enter a letter : ").lower()

        if(choose == "a"):
            rectangle()
        elif(choose == "b"):
            circle()
        elif(choose == "c"):
            trapezoid()
        elif(choose == "d"):
            triangle()
        else:
            print("Invalid try again")
            return False


start()