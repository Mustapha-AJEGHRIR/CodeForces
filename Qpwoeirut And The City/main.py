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
    n = int(input())
    heights = list(map(int, input().split()))
    
    if n % 2 == 1: # Only one possible configuration for odd number of buildings
        cost = 0
        for i in range(1, n-1, 2):    # 1 to n-1, jump the gap each time
            cost += max(0, max(heights[i-1], heights[i+1]) - heights[i] + 1)
        print(cost)
    else : 
        """
        We have a lot of configurations here, we have the right to jump 1 more building among the ones we have to build.
        """
        # cost_first = [max(heights[i-1], heights[i+1]) - heights[i] + 1 for i in range(1, n, 2)]
        # cost_end = [max(heights[i-1], heights[i+1]) - heights[i] + 1 for i in range(2, n, 2)]
        cum_cost_first = []
        cum_cost_end = []
        
        cum_cost = 0
        for i in range(1, n-1, 2):
            cum_cost += max(0, max(heights[i-1], heights[i+1]) - heights[i] + 1)
            cum_cost_first.append(cum_cost)
            
        cum_cost = 0
        for i in range(n-1 -1, 1, -2):
            cum_cost += max(0, max(heights[i-1], heights[i+1]) - heights[i] + 1)
            cum_cost_end.append(cum_cost)
        cum_cost_end.reverse()
        
        # find the best split
        min_cost = min(cum_cost_first[-1], cum_cost_end[0])
        for i in range(1, len(cum_cost_first)):
            min_cost = min(min_cost, cum_cost_first[i-1] + cum_cost_end[i])
        print(min_cost)