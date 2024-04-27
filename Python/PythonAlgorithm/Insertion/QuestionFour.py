# Example 4: Sorting a list of tuples
#
# Input: [(3, 'c'), (1, 'a'), (2, 'b'), (4, 'd'), (0, 'e')]
# Output: [(0, 'e'), (1, 'a'), (2, 'b'), (3, 'c'), (4,/ 'd/')]


def insertion_sort(arrTuple):
    for i in range(1, len(arrTuple)):
        j = i
        while arrTuple[j - 1] > arrTuple[j] and j > 0:
            arrTuple[j - 1], arrTuple[j] = arrTuple[j], arrTuple[j - 1]
            j -= 1

arrTuple = [(3, 'c'), (1, 'a'), (2, 'b'), (4, 'd'), (0, 'e')]
insertion_sort(arrTuple)
print(arrTuple)

