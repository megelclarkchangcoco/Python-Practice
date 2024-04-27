# Example 3: Sorting a list of floating-point numbers
#
# Input: [3.14, 1.618, 2.718, 0.577, 1.414]
# Output: [0.577, 1.414, 1.618, 2.718, 3.14]
# Example 4: Sorting a list of tuples

import time

def selection_sort(arr):
    total_time = 0
    for i in range(0, len(arr) - 1):
        start_time = time.time()
        cur_min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_min_index]:
                cur_min_index = j

        arr[i], arr[cur_min_index] = arr[cur_min_index], arr[i]
    end_time = time.time()
    iteration = (end_time - start_time) * 1000
    total_time += iteration
    print("Execution time : ", total_time, " ms")




arr = [3.14, 1.618, 2.718, 0.577, 1.414]
selection_sort(arr)
print(arr)
