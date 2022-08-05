"""
You are given a positive integer n.

The weight of a permutation p1,p2,…,pn is the number of indices 1≤i≤n such that i divides pi. Find a permutation p1,p2,…,pn with the minimum possible weight (among all permutations of length n).

A permutation is an array consisting of n distinct integers from 1 to n in arbitrary order. For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array) and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤104). The description of the test cases follows.

The only line of each test case contains a single integer n (1≤n≤105) — the length of permutation.

It is guaranteed that the sum of n over all test cases does not exceed 105.

Output
For each test case, print a line containing n integers p1,p2,…,pn so that the permutation p has the minimum possible weight.

If there are several possible answers, you can print any of them.
"""

t=int(input())


# def find_lowest_div(p, I):
#     one_is_there = False
#     for _ in range(len(I)-1 -1 , -1, -1 ):          # reading from the end
#         i = I[_]
#         if i == 1 :
#             one_is_there = True
#             continue
#         if p%i == 0:
#             I.remove(i)
#             return i
#     if one_is_there :
#         I.remove(1)
#         return 1
#     else : # It should be di
#         last 



for case in range(t):
    n = int(input())
    
    # P = list(range(1, n+1))
    # I = reversed(list(range(1, n+1)))               # easier when reading from the end
    
    # pairs = []
    # for p in P :
        
    print(n, *range(1, n))