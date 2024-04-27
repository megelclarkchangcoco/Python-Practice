# return statement = functions send python values/object back to the caller
#                     These values/object are known as the fuction's return value'



def recursion(num1, num2):
    return num1 *  num2

x  = 2 * 10

print(x)

def another(recursion, num2):
    return recursion * num2

z = x * 20

print(z)
