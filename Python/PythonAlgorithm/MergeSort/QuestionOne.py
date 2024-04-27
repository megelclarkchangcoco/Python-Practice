# How would you implement merge sort in Python to sort a list of integers in ascending order? For instance, if the input list is [3, 1, 5, 2, 4],
# what would be the sorted output list?
# Input: [3, 1, 5, 2, 4]
# Output: [1, 2, 3, 4, 5]


def merge_sort(arr):
    # Check if the length of the array is greater than 1
   if len(arr) > 1:
    # Divide the array into two halves
    left_arr = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]

    #Recursivly
    merge_sort(left_arr)
    merge_sort(right_arr)

    #merge the sorted halves
    i = 0
    j = 0
    k = 0
    while i < len(left_arr) and j < len(right_arr):
        # Compare elements from both havles and merge them into the original way
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[j];
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    #copy the remaining elements of left_arra if any
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of right_arr if any
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1



arr = [3, 1, 5, 2, 4]
merge_sort(arr)
print(arr)
