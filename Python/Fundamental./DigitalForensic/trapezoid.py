#QUESTION : c) Area of a trapezad

import math
# calculate trapezoid shape
def trapezoid():
    # while loop to repeatedly perform calculatiom
    while(True):
        baseOne = int(input("Enter a number of  base one :"))
        baseTwo = int(input("Enter a number of base two :"))
        height = int(input("Entter a number of Height : "))

        area = ((baseOne + baseTwo) / 2) * height
        print(f"base of trapezoid {area}")

        # ask if want calculate again
        ask = str(input("You want calculate again? (yes or no): "))
        if(ask == "no"):
            print("Thankyou")
            return False


trapezoid()


