"""
You have a sequence of n colored blocks. The color of the i-th block is ci, an integer between 1 and n.

You will place the blocks down in sequence on an infinite coordinate grid in the following way.

Initially, you place block 1 at (0,0).
For 2≤i≤n, if the (i−1)-th block is placed at position (x,y), then the i-th block can be placed at one of positions (x+1,y), (x−1,y), (x,y+1) (but not at position (x,y−1)), as long no previous block was placed at that position.
A tower is formed by s blocks such that they are placed at positions (x,y),(x,y+1),…,(x,y+s−1) for some position (x,y) and integer s. The size of the tower is s, the number of blocks in it. A tower of color r is a tower such that all blocks in it have the color r.

For each color r from 1 to n, solve the following problem independently:

Find the maximum size of a tower of color r that you can form by placing down the blocks according to the rules.
Input
The first line contains a single integer t (1≤t≤104) — the number of test cases.

The first line of each test case contains a single integer n (1≤n≤105).

The second line of each test case contains n integers c1,c2,…,cn (1≤ci≤n).

It is guaranteed that the sum of n over all test cases does not exceed 2⋅105.

Output
For each test case, output n integers. The r-th of them should be the maximum size of an tower of color r you can form by following the given rules. If you cannot form any tower of color r, the r-th integer should be 0.
"""

# import numpy as np

def get_matrix_zeros(n,m):
    matrix = []
    for i in range(n):
        matrix.append([0]*m)
    return matrix
def get_max(matrix):
    maxi = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > maxi:
                maxi = matrix[i][j]
    return maxi

t = int(input())

# for case in range(t):
#     n = int(input())
#     blocks = [int(x) for x in input().split()]
    
#     color_max_height = []    
#     for color in range(n):
#         m = max(blocks) +1
#         matrix = get_matrix_zeros(m, n)
#         for height in range(m): # rows of matrix
#             for block in range(n): # colomns of matrix
#                 if blocks[block]-1 != color : # the default value of the matrix is 0
#                     continue 
#                 else :
#                     value = 1
#                     i, j = height, block
#                     while j-1>=0 and i-1>=0:
#                         value = max(value, matrix[i-1][j-1] + 1)
#                         j = j-2
#                     matrix[height][block] = value
#         # print("\t", color, "\t\n", matrix)
#         color_max_height.append(int(get_max(matrix)))
#     print(*color_max_height)

for case in range(t):
    n = int(input())
    blocks = [int(x) for x in input().split()]
    
    color_max_height = []    
    for color in range(n):
        tower_heights = [0]*n
        for block in range(n): 
            if blocks[block]-1 != color : # the default value of height is 0
                continue 
            else :
                # value = 1
                # candidats = tower_heights[:block]
                # candidats.reverse()
                # candidats = candidats[::2]
                # best_candidats = max(candidats) if len(candidats) > 0 else 0
                # value = max(value, best_candidats + 1)
                value = 1
                i = block
                while i-1>=0:
                    value = max(value, tower_heights[i-1] + 1)
                    i = i-2
                tower_heights[block] = value
        # print("\t", color, "\t\n", matrix)
        color_max_height.append(int(max(tower_heights)))
    print(*color_max_height)