"""
You are given an array a consisting of n positive integers.

You are allowed to perform this operation any number of times (possibly, zero):

choose an index i (2≤i≤n), and change ai to ai−ai−1.
Is it possible to make ai=0 for all 2≤i≤n?

Input
The input consists of multiple test cases. The first line contains a single integer t (1≤t≤100)  — the number of test cases. The description of the test cases follows.

The first line contains one integer n (2≤n≤100) — the length of array a.

The second line contains n integers a1,a2,…,an (1≤ai≤109).

Output
For each test case, print "YES" (without quotes), if it is possible to change ai to 0 for all 2≤i≤n, and "NO" (without quotes) otherwise.

You can print letters in any case (upper or lower).
"""


t =  int(input())

for case in range(t):
    