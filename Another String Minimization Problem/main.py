"""
You have a sequence a1,a2,…,an of length n, consisting of integers between 1 and m. You also have a string s, consisting of m characters B.

You are going to perform the following n operations.

At the i-th (1≤i≤n) operation, you replace either the ai-th or the (m+1−ai)-th character of s with A. You can replace the character at any position multiple times through the operations.
Find the lexicographically smallest string you can get after these operations.

A string x is lexicographically smaller than a string y of the same length if and only if in the first position where x and y differ, the string x has a letter that appears earlier in the alphabet than the corresponding letter in y.

Input
The first line contains the number of test cases t (1≤t≤2000).

The first line of each test case contains two integers n and m (1≤n,m≤50) — the length of the sequence a and the length of the string s respectively.

The second line contains n integers a1,a2,…,an (1≤ai≤m) — the sequence a.

Output
For each test case, print a string of length m — the lexicographically smallest string you can get. Each character of the string should be either capital English letter A or capital English letter B.
"""

t = int(input())
for case in range(t):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    seq = ["B"] * m
    for i in range(n):
        i_1, i_2 = numbers[i], m + 1 - numbers[i]
        min_i = min(i_1, i_2)
        max_i = max(i_1, i_2)
        if seq[min_i - 1] == "B":
            seq[min_i - 1] = "A"
        else :
            seq[max_i - 1] = "A"
    print("".join(seq))