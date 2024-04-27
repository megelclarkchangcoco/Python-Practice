# 4. Tuple Question:
#
# Question: Write a Python program that takes two tuples of integers as input representing coordinates (x1, y1) and (x2, y2) respectively, and calculates the Euclidean distance between the two points.
#
# Sample Input: (1, 2), (4, 6)
#
# Sample Output: 5.0
import math

import math

def euclidean_distance(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return float(distance)

point1 =(1,2)
point2 = (4,6)
distance = euclidean_distance(point1, point2)
print(distance)
