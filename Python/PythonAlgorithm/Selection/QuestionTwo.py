# Example 2: Sorting a list of strings
#
# Input: ['banana', 'apple', 'orange', 'grape', 'kiwi']
# Output: ['apple', 'banana', 'grape', 'kiwi', 'orange']

import time

def selection_sort(arr):
    total_time = 0

    for i in range(0, len(arr) - 1 ):
        start_time = time.time()
        cur_min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_min_index]:
                cur_min_index = j

        arr[i], arr[cur_min_index] = arr[cur_min_index], arr[i]
        end_time = time.time()
        iteration_time = (end_time - start_time) * 1000  # Convert to milliseconds
        total_time += iteration_time

    print("Execution Time : ", total_time, "ms")

arr = ['banana', 'apple', 'orange', 'grape', 'kiwi']
selection_sort(arr)
print(arr)

