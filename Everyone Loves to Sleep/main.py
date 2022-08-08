"""
Vlad, like everyone else, loves to sleep very much.

Every day Vlad has to do n things, each at a certain time. For each of these things, he has an alarm clock set, the i-th of them is triggered on hi hours mi minutes every day (0≤hi<24,0≤mi<60). Vlad uses the 24-hour time format, so after h=12,m=59 comes h=13,m=0 and after h=23,m=59 comes h=0,m=0.

This time Vlad went to bed at H hours M minutes (0≤H<24,0≤M<60) and asks you to answer: how much he will be able to sleep until the next alarm clock.

If any alarm clock rings at the time when he went to bed, then he will sleep for a period of time of length 0.

Input
The first line of input data contains an integer t (1≤t≤100) — the number of test cases in the test.

The first line of the case contains three integers n, H and M (1≤n≤10,0≤H<24,0≤M<60) — the number of alarms and the time Vlad went to bed.

The following n lines contain two numbers each hi and mi (0≤hi<24,0≤mi<60) — the time of the i alarm. It is acceptable that two or more alarms will trigger at the same time.

Numbers describing time do not contain leading zeros.

Output
Output t lines, each containing the answer to the corresponding test case. As an answer, output two numbers  — the number of hours and minutes that Vlad will sleep, respectively. If any alarm clock rings at the time when he went to bed, the answer will be 0 0.
"""


def compare_clocks(h1, m1, h2, m2):
    """
    return 1 if 1 is higher than 2. 0 for equality and -1 for the opposite
    """
    if h1 > h2 :
        return 1
    elif h2 > h1 :
        return -1
    else :
        if m1 > m2 :
            return 1
        elif m2 > m1 :
            return -1
        else :
            return 0

class Clock():
    def __init__(self, h, m):
        self.h = h
        self.m = m
    def __eq__(self, other):
        return compare_clocks(self.h, self.m, other.h, other.m) == 0 
    def __ne__(self, other):
        return not self.__eq__(other)
    def __gt__(self, other):
        return compare_clocks(self.h, self.m, other.h, other.m) == 1 
    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)
    def __le__(self, other):
        return not self.__gt__(other)
    def __lt__(self, other):
        return not self.__ge__(other)
    
    def __sub__(self, other):
        minutes_1 = self.h * 60 + self.m 
        minutes_2 = other.h * 60 + other.m
        
        diff = minutes_1 - minutes_2
        return Clock(diff//60, diff%60)
    
    def __add__(self, other):
        minutes_1 = self.h * 60 + self.m 
        minutes_2 = other.h * 60 + other.m
        
        add = minutes_1 + minutes_2
        return Clock(add//60, add%60)
    
    def __repr__(self):
        return str(self.h) + " " + str(self.m)

t = int(input())

for case in range(t):
    n, H, M = map(int, input().split())
    
    main_clock = Clock(H, M)
    clocks = [ Clock( *map(int, input().split()) ) for _ in range(n)]
    clocks.sort()
    
    clocks_filtered = list(filter(lambda x: x>=main_clock, clocks))

    if clocks_filtered :
        print(clocks_filtered[0] - main_clock)
    else :
        clk = clocks[0] + Clock(24, 0)
        print(clk - main_clock)

    