# Iterable = an object/collection that can return its elements one at a time,
#           allowing it to be iterated over in a loop

def item():
    numbers = [1, 2, 3, 4, 5]

    for number in numbers:
        print(number)
    print()

    for reverse in numbers:
        print(reverse, end = "-")
    print()


item()