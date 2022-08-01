"""
Qpwoeirut has taken up architecture and ambitiously decided to remodel his city.

Qpwoeirut's city can be described as a row of n buildings, the i-th (1≤i≤n) of which is hi floors high. You can assume that the height of every floor in this problem is equal. Therefore, building i is taller than the building j if and only if the number of floors hi in building i is larger than the number of floors hj in building j.

Building i is cool if it is taller than both building i−1 and building i+1 (and both of them exist). Note that neither the 1-st nor the n-th building can be cool.

To remodel the city, Qpwoeirut needs to maximize the number of cool buildings. To do this, Qpwoeirut can build additional floors on top of any of the buildings to make them taller. Note that he cannot remove already existing floors.

Since building new floors is expensive, Qpwoeirut wants to minimize the number of floors he builds. Find the minimum number of floors Qpwoeirut needs to build in order to maximize the number of cool buildings.

Input
The first line contains a single integer t (1≤t≤104) — the number of test cases.

The first line of each test case contains the single integer n (3≤n≤105) — the number of buildings in Qpwoeirut's city.

The second line of each test case contains n integers h1,h2,…,hn (1≤hi≤109) — the number of floors in each of the buildings of the city.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅105.

Output
For each test case, print a single integer — the minimum number of additional floors Qpwoeirut needs to build in order to maximize the number of cool buildings.
"""

t = int(input())

for case in range(t):
    pass