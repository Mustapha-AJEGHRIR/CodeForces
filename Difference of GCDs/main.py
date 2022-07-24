"""
You are given three integers n, l, and r. You need to construct an array a1,a2,…,an (l≤ai≤r) such that gcd(i,ai) are all distinct or report there's no solution.

Here gcd(x,y) denotes the greatest common divisor (GCD) of integers x and y.

Input
The input consists of multiple test cases. The first line contains a single integer t (1≤t≤104) — the number of test cases. The description of the test cases follows.

The first line contains three integers n, l, r (1≤n≤105, 1≤l≤r≤109).

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case, if there is no solution, print "NO" (without quotes). You can print letters in any case (upper or lower).

Otherwise, print "YES" (without quotes). In the next line, print n integers a1,a2,…,an — the array you construct.

If there are multiple solutions, you may output any.

"""

# from unicodedata import decomposition


# def is_prime(x):
#     root = int(x**0.5) + 1
#     for i in range(2, root):
#         if x % i == 0:
#             return False
#     return True

# LIMIT_PRIME_NUMBER = 1e5
# PRIME_NUMBERS = [x for x in range(LIMIT_PRIME_NUMBER) if is_prime(x)]
# PRIME_NUMBERS_set = set(PRIME_NUMBERS)


t = int(input())


# def prime_dividers(n : int):
#     root = int(n**0.5) + 1
#     # small prime dividers
#     p_dividers = []
#     for p in PRIME_NUMBERS:
#         if p >= root:
#             break
#         if n % p == 0:
#             p_dividers.append(p)
#             # large prime dividers
#             large_div = n//p
#             if large_div in PRIME_NUMBERS_set:
#                 p_dividers.append(large_div)
#     return p_dividers

# def filter_dividers(dividers, l, r):
#     """
#     test if a divider in diveders has a multiple in [l, r]
#     """
#     f_dividers = []
#     for div in dividers :
#         other = div // l + 1
#         multiple = div * other
#         if multiple >= l and multiple <= r:
#             f_dividers.append(div)
#     return f_dividers

    
# for case in range(t):
#     n, l , r = map(int, input().split())
    
# for s in[*open(0)][1:]:
    # n,l,r=map(int,s.split())

for case in range(t):
    n,l,r=map(int,input().split())
    f=min(a:=[r-r%i for i in range(1,n+1)])>=l
    print('NYOE S'[f::2],*a*f)