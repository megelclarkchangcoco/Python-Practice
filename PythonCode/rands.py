
import random

def rockpaperscissors():
    list = ['Rock', 'paper', 'Scissors']
    z = random.choice(list)
    print(z)

rockpaperscissors()


def cards():
    cards = [1,2,3,4,5,6,7,8,9,10,'Jack','Queen', 'King']
    random.shuffle(cards)
    print(cards)

cards()
