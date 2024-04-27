# 2. List Question:
#
# Question: Write a Python program that takes a list of integers as input and prints the sum of all the elements in the list.
#
# Sample Input: [1, 2, 3, 4, 5]
#
# Sample Output: 15

total = 0
n =  [1,2,3,4,5]


for i in range(len(n)):
    total = total + n[i]

print(total)
