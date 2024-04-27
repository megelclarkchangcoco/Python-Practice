# args = parameter that will pack  all arguments into a tuoke
#         useful so that a function can accept a varying amount of arguments


def addNum(*args):
    sum = 0
    args = list(args)
    args[0] = 0
    for i in args:
        sum += i
    return sum

print(addNum(1,2,3,4,5,6,7,8,9,10))
