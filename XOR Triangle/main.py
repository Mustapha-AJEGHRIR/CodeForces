"""
You are given a positive integer n. Since n may be very large, you are given its binary representation.

You should compute the number of triples (a,b,c) with 0≤a,b,c≤n such that a⊕b, b⊕c, and a⊕c are the sides of a non-degenerate triangle.

Here, ⊕ denotes the bitwise XOR operation.

You should output the answer modulo 998244353.

Three positive values x, y, and z are the sides of a non-degenerate triangle if and only if x+y>z, x+z>y, and y+z>x.

Input
The first and only line contains the binary representation of an integer n (0<n<2200000) without leading zeros.

For example, the string 10 is the binary representation of the number 2, while the string 1010 represents the number 10.

Output
Print one integer — the number of triples (a,b,c) satisfying the conditions described in the statement modulo 998244353.
"""

# take a look at here https://codeforces.com/blog/entry/105236

modulo_to = 998244353
# n = 