# Example 1: Sorting a list of integers
#
# Input: [5, 2, 9, 1, 6]
# Output: [1, 2, 5, 6, 9]

import time

def selection_sort(arr):
    total_time = 0

    for i in range(0, len(arr) - 1):
        start_time = time.time()
        cur_min_index = i
        for j in range(i + 1 , len(arr)):
            if arr[j] < arr[cur_min_index]:
               cur_min_index = j

        arr[i], arr[cur_min_index] = arr[cur_min_index], arr[i]

    end_time = time.time()
    iteration = end_time - start_time
    total_time += iteration
    print("Execution time : ", total_time, " seconds")

arr = [5, 2, 9, 1, 6]
selection_sort(arr)
print(arr)
