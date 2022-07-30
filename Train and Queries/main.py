"""
Along the railroad there are stations indexed from 1 to 109. An express train always travels along a route consisting of n stations with indices u1,u2,…,un, where (1≤ui≤109). The train travels along the route from left to right. It starts at station u1, then stops at station u2, then at u3, and so on. Station un — the terminus.

It is possible that the train will visit the same station more than once. That is, there may be duplicates among the values u1,u2,…,un.

You are given k queries, each containing two different integers aj and bj (1≤aj,bj≤109). For each query, determine whether it is possible to travel by train from the station with index aj to the station with index bj.

For example, let the train route consist of 6 of stations with indices [3,7,1,5,1,4] and give 3 of the following queries:

a1=3, b1=5
It is possible to travel from station 3 to station 5 by taking a section of the route consisting of stations [3,7,1,5]. Answer: YES.

a2=1, b2=7
You cannot travel from station 1 to station 7 because the train cannot travel in the opposite direction. Answer: NO.

a3=3, b3=10
It is not possible to travel from station 3 to station 10 because station 10 is not part of the train's route. Answer: NO.

Input
The first line of the input contains an integer t (1≤t≤104) —the number of test cases in the test.

The descriptions of the test cases follow.

The first line of each test case is empty.

The second line of each test case contains two integers: n and k (1≤n≤2⋅105,1≤k≤2⋅105) —the number of stations the train route consists of and the number of queries.

The third line of each test case contains exactly n integers u1,u2,…,un (1≤ui≤109). The values u1,u2,…,un are not necessarily different.

The following k lines contain two different integers aj and bj (1≤aj,bj≤109) describing the query with index j.

It is guaranteed that the sum of n values over all test cases in the test does not exceed 2⋅105. Similarly, it is guaranteed that the sum of k values over all test cases in the test also does not exceed 2⋅105

Output
For each test case, output on a separate line:

YES, if you can travel by train from the station with index aj to the station with index bj
NO otherwise.
You can output YES and NO in any case (for example, strings yEs, yes, Yes and YES will be recognized as a positive response).
"""


t = int(input())


for case in range(t):
    input() # empty line
    n, k = map(int, input().split())
    
    # stations = list(map(int, input().split()))
    stations = input().split()
    
    # --------------------------- collect the positions -------------------------- #
    # positions = {station : [None, None] for station in set(stations)}
    # for i in range(n):
    #     limits = positions[stations[i]]
    #     if limits[0] is None:
    #         limits[0] = i       # The fisrt found index
    #         limits[1] = i
    #     else:
    #         limits[1] = i       # The last found index
    l_positions = {str(station) : n for station in set(stations)}
    r_positions = {str(station) : -1 for station in set(stations)}
    for i, id in enumerate(stations):
        l_positions[str(id)] = min(l_positions[str(id)], i)
        r_positions[str(id)] = i
        
    # # ------------------------------ sort positions ------------------------------ #
    # for station in positions:
    #     positions[station].sort()
        
    # ----------------------- make the verification faster ----------------------- #
    # positions_set = set(positions.keys())
    
    for query in range(k):
        # l_sta, r_sta = map(int, input().split())
        l_sta, r_sta = input().split()
        if l_positions.get(l_sta, n) > r_positions.get(r_sta, -1):
            print("NO")
        else:
            print("YES")
        
    # for query in range(k):
    #     l_sta, r_sta = map(int, input().split())
    #     # possible = False
    #     # if l_sta in positions and r_sta in positions:
    #         # for l_pos in positions[l_sta]:
    #         #     for r_pos in positions[r_sta]:
    #         #         if l_pos < r_pos :
    #         #             possible = True
    #         #             break
    #         #     else:
    #         #         # inner loop was not broken
    #         #         continue
    #         #     # inner loop was broken, break outer loop
    #         #     break 
    #     l_pos = positions.get(l_sta, [1e10])[0]
    #     r_pos = positions.get(r_sta, [-1])[-1]
    #     print("YES" if l_pos < r_pos else "NO")
    #     # else : 
    #     #     print("NO")
    