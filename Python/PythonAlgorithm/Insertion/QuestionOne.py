# Example 1: Sorting a list of integers
#
# Input: [5, 2, 9, 1, 6]
# Output: [1, 2, 5, 6, 9]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

arr = [5,2,9,1,6]
insertion_sort(arr)
print(arr)
