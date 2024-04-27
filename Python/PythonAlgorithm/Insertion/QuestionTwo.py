# Input: ['banana', 'apple', 'orange', 'grape', 'kiwi']
# Output: ['apple', 'banana', 'grape', 'kiwi', 'orange']
# Example 3: Sorting a list of floating-point numbers


def insertion_fruit(arrFruit):
    for i in range(1, len(arrFruit)):
        j = i
        while arrFruit[j - 1] > arrFruit[j] and j > 0:
            arrFruit[j - 1], arrFruit[j] = arrFruit[j], arrFruit[j - 1]
            j -= 1

arrFruit = ['banana', 'apple', 'orange', 'grape', 'kiwi']
insertion_fruit(arrFruit)
print(arrFruit)
