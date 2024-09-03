# Question : a) Area of a triangle

def get_area():

    while(True):
        base = int(input("Enter the Base of Triangle:"))
        height = int(input("Enter the Height of Triangle:"))

        area = 0.5 * base * height # computation of area

        print(area) #print
        # ask again
        ask = input("do you want try again?  (yes or no):").lower()

        if(ask == "no"):
            return False


get_area() # excute function get_area