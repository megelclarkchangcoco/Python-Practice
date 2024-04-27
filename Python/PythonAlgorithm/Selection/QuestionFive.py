


# Example 5: Sorting a list of dictionaries
#
# Input: [ {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}, {'name': 'David', 'age': 35}, {'name': 'Eve', 'age': 28} ]
# Output: [ {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}, {'name': 'David', 'age': 35}, {'name': 'Eve', 'age': 28} ]
# (Since dictionaries are unordered in Python, the output would be the same as the input, but the list of dictionaries would be sorted based on their key-value pairs if applicable.)

import time

def selection_sort(arrTuple):
    total_time = 0
    for i in range(0, len(arrTuple) - 1):
        start_time = time.time()
        cur_min_index = i
        for j in range(i + 1, len(arrTuple)):
            if arrTuple[j]['name'] < arrTuple[cur_min_index]['name']:  # Comparing based on 'age' key
                cur_min_index = j  # Update the index of the minimum element
        arrTuple[i], arrTuple[cur_min_index] = arrTuple[cur_min_index], arrTuple[i]
    end_time = time.time()
    iteration = (end_time - start_time ) * 1000
    total_time += iteration
    print("Execution time : ", total_time, " ms")



arrTuple = [
    {'name': 'Bob', 'age': 30},
    {'name': 'Alice', 'age': 25},
    {'name': 'Charlie', 'age': 20},
    {'name': 'Bob', 'age': 30},
    {'name': 'David', 'age': 35}
]
selection_sort(arrTuple)
print(arrTuple)
