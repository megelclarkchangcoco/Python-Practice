def merge_sort(arr):
    # Check if the length of the array is greater than 1
    if len(arr) > 1:
        # Divide the array into two halves
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # Recursively sort the two halves
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Merge the sorted halves
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            # Compare elements from both halves and merge them into the original array
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_arr if any
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # Copy the remaining elements of right_arr if any
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

# Example usage
arr = [5,6,2,4,3,1]
merge_sort(arr)
print(arr)
