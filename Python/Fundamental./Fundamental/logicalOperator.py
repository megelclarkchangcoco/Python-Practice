# logical operator (and, or) = used to check if two or more conditional statemetns is true


age = int(input("What is your age? :"))


if age  >= 18 and age <= 100:
    print("Good News Mr/Ms")
    print("You Can Vote at that age!")
elif age <= 0 and age <= 17:
    print("Oh, Sorry !")
    print("you can't vote")
