
import time

def selection_sort(arr):
    total_time = 0
    # Iterate over the list except the last element
    for i in range(0, len(arr) - 1):
        start_time = time.time()
        # Assume the current index has the minimum value
        cur_min_idx = i
        # Iterate over the unsorted part of the list
        for j in range(i + 1, len(arr)):
            # Check if any element is smaller than the assumed minimum
            if arr[j] < arr[cur_min_idx]:
                # If found, update the index of the minimum element
                cur_min_idx = j

        # Swap the current minimum element with the first unsorted element
        arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]

    end_time = time.time() # Record the end time
    iteration_time = end_time - start_time
    total_time += iteration_time
    print("Execution time:", total_time, "seconds")  # Output the execution time


arr = [5,4,1,2,3,7,10,11,8,9,13,15,17,12,16,20,19,18]
selection_sort(arr)
print(arr)  # Output the sorted array
