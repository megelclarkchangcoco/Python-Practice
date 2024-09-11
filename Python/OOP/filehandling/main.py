# exception = An event that interrupts the flow of a program
#              (zeroDivisionError, TypeError, ValueError)
#              1. Try, 2. except, 3.finally
from typing import final

try:
    number = int(input("Enter a number :"))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero boss!")
except ValueError:
    print("Enter only number please!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here")
