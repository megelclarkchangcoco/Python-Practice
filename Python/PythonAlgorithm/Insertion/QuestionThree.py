# Example 3: Sorting a list of floating-point numbers
# Input: [3.14, 1.618, 2.718, 0.577, 1.414]
# Output: [0.577, 1.414, 1.618, 2.718, 3.14]


def insertion_sort(arrFloat):
    for i in range(1, len(arrFloat)):
        j = i
        while arrFloat[j - 1]> arrFloat[j] and j > 0:
            arrFloat[j - 1], arrFloat[j] = arrFloat[j], arrFloat[j - 1]
            j -=  1

arrFloat = [3.14, 1.618, 2.718, 0.577, 1.414]
insertion_sort(arrFloat)
print(arrFloat)
