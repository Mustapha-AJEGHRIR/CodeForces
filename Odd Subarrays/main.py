"""
For an array [b1,b2,…,bm] define its number of inversions as the number of pairs (i,j) of integers such that 1≤i<j≤m and bi>bj. Let's call array b odd if its number of inversions is odd.

For example, array [4,2,7] is odd, as its number of inversions is 1, while array [2,1,4,3] isn't, as its number of inversions is 2.

You are given a permutation [p1,p2,…,pn] of integers from 1 to n (each of them appears exactly once in the permutation). You want to split it into several consecutive subarrays (maybe just one), so that the number of the odd subarrays among them is as large as possible.

What largest number of these subarrays may be odd?

Input
The first line of the input contains a single integer t (1≤t≤105)  — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (1≤n≤105)  — the size of the permutation.

The second line of each test case contains n integers p1,p2,…,pn (1≤pi≤n, all pi are distinct)  — the elements of the permutation.

The sum of n over all test cases doesn't exceed 2⋅105.

Output
For each test case output a single integer  — the largest possible number of odd subarrays that you can get after splitting the permutation into several consecutive subarrays.
"""

t = int(input())

for case in range(t):
    n = int(input())
    permutations = list(map(int, input().split()))
    