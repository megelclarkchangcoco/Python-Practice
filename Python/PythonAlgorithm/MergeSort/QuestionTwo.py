# Can you illustrate the implementation of merge sort in Python for sorting a
# list of strings in lexicographic order? Suppose the input list is ['banana', 'apple', 'orange', 'grape'],
# what would be the sorted output list?
# Input: ['banana', 'apple', 'orange', 'grape']
# Output: ['apple', 'banana', 'grape', 'orange']
import time

def merge_sort(arr):
    total_time = 0
    if len(arr) > 1:

        left_arr = arr[: len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)


        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):

            if left_arr[i] < right_arr[j]:
                start_time = time.time()
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

            end_time = time.time()
            iteration = (end_time - start_time) * 1000
            total_time += iteration

            print(total_time)


arr = ['banana', 'apple', 'orange', 'grape']
merge_sort(arr)
print(arr)
