

#
# Example 4: Sorting a list of tuples
#
# Input: [(3, 'c'), (1, 'a'), (2, 'b'), (4, 'd'), (0, 'e')]
# Output: [(0, 'e'), (1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

import time

def selection_sort(arr):
    total_time = 0
    for i in range(0, len(arr) -1 ):
        start_time = time.time()
        cur_min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_min_index]:
                cur_min_index -= j
        arr[i], arr[cur_min_index] = arr[cur_min_index], arr[i]
    end_time = time.time()
    itearation = (end_time - start_time) * 1000
    total_time += itearation
    print("Execution time :", total_time, " ms")
arr = [(3, 'c'), (1, 'a'), (2, 'b'), (4, 'd'), (0, 'e')]
selection_sort(arr)
print(arr)

