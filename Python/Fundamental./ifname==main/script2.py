from script1 import *


def favorite_drink(drink):
    print(f"ypur favovrite drink is {drink}")

def main():
    print("this is script 2 ")
    favorite_food("sushi")
    favorite_drink("coffee")
    print("Goodbye")

if __name__ == '__main__':
    main()