
# 3. 2D List Question:
#
# Question: Write a Python program that takes a 2D list of integers as input and prints the transpose of the matrix.
#
# Sample Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# Sample Output:
# 1 4 7
# 2 5 8
# 3 6 9

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        print(matrix[i][j], end=' ')
    print()
