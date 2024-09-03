# list comprehension = a concise way to create lists in Python
#                      compact and easier to read than traditional loops
#                      [expression for a value in iterable if condition]


double = []
for x in range(1, 11):
    double.append(x * 2)

print(double)

doubles = [x * 2 for x in range(1,11)]

print(doubles)