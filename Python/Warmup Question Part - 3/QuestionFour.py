# Question Four:Function
# Function Question:
# Write a Python function that takes a list of numbers as input and returns a new list containing only the even numbers.
#
# Sample Input:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# Sample Output:
# [2, 4, 6, 8, 10]


def evenNum(nums):
    result = []
    for i in nums:
        if i % 2 == 0:
            result.append(i)
    return result


numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = evenNum(numbers)
print(even_numbers)
