# Input: [ {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}, {'name': 'David', 'age': 35}, {'name': 'Eve', 'age': 28} ]
# Output: [ {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}, {'name': 'David', 'age': 35}, {'name': 'Eve', 'age': 28} ]
# (Since dictionaries are unordered in Python, the output would be the same as the input, but the list of dictionaries would be sorted based on their key-value pairs if applicable.)




def insertion_sort(name):
    # Iterate over each element in the list starting from the second element (index 1)
    for i in range(1, len(name)):
        j = i
        # While the current element is less than the previous one and we haven't reached the beginning of the list
        while j > 0 and name[j - 1]['name'] > name[j]['name']:
            # Swap the current element with the previous one
            name[j - 1], name[j] = name[j], name[j - 1]
            # Move to the previous element
            j -= 1

# List of dictionaries representing names and ages
name = [{'name': 'Alice', 'age': 25}, {'name': 'Eve', 'age': 28}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20},
        {'name': 'David', 'age': 35}]

# Call the insertion_sort function to sort the list of dictionaries based on the 'name' key
insertion_sort(name)

# Print the sorted list
print(name)

