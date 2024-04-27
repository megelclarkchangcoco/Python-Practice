# Question one : sets
#
# Write a Python program that takes two sets of integers as input and prints the intersection of the two sets.
#
# Sample Input:
# {1, 2, 3}, {2, 3, 4}
#
# Sample Output:
# {2, 3}


num = [{1,2,3}, {2,3,4}]

numRemove = 4
res = []


for i in num:
    i = list(i)
    while numRemove in i:
      i.remove(numRemove)
      res.append(tuple(i))
print(str(res))


