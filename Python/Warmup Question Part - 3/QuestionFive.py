# Question Five:Function
# Write a Python function that takes a string as input and returns a dictionary where keys are characters and values are the count of each character in the string.
#
# Sample Input:
# 'hello'
#
# Sample Output:
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def dicHello(name):
    count = {}
    for i in name:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

results = dicHello('hello')
print(results)
