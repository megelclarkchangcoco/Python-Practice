# exception = events detected during execution that interrupt the flow of a program


try:
    numerator = int(input("Enter a number to devide "))
    denominator = int(input("Enter a number to devider: "))
    result = numerator / denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("you can't dived by zero idiot!!!!!!!!!!!!")
except ValueError as e :
    print(e)
    print("Enter only number ")
except Exception as e :
    print(e)
    print("Error")
else:
    print(result)
finally:
    print("this will always execute!")
