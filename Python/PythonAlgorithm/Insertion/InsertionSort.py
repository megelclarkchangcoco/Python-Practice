
import time

def insertion_sort(arr):
    start_time = time.time()
    for i in range(1, len(arr)):  # Iterate through the list starting from the second element
        j = i  # Set j to the current index i
        while arr[j - 1] > arr[j] and j > 0:  # Continue swapping until the current element is in the correct position
            arr[j - 1], arr[j] = arr[j], arr[j - 1]  # Swap the elements
            j -= 1  # Move j towards the beginning of the list
            # The above steps effectively move the current element to its correct sorted position
            # and shift larger elements to the right
            # The loop exits when either the element is in its correct position or j reaches 0
            # This process is repeated for each element in the list, resulting in a sorted list
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:  ", execution_time, " seconds")

arr = [6,1,2,4,5,3]  # The input list
insertion_sort(arr)  # Sort the list using insertion sort
print(arr)  # Print the sorted list














