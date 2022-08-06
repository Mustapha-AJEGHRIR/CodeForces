"""
There are three doors in front of you, numbered from 1 to 3 from left to right. Each door has a lock on it, which can only be opened with a key with the same number on it as the number on the door.

There are three keys — one for each door. Two of them are hidden behind the doors, so that there is no more than one key behind each door. So two doors have one key behind them, one door doesn't have a key behind it. To obtain a key hidden behind a door, you should first unlock that door. The remaining key is in your hands.

Can you open all the doors?

Input
The first line contains a single integer t (1≤t≤18) — the number of testcases.

The first line of each testcase contains a single integer x (1≤x≤3) — the number on the key in your hands.

The second line contains three integers a,b and c (0≤a,b,c≤3) — the number on the key behind each of the doors. If there is no key behind the door, the number is equal to 0.

Values 1,2 and 3 appear exactly once among x,a,b and c.

Output
For each testcase, print "YES" if you can open all the doors. Otherwise, print "NO".
"""



t=int(input())

for case in range(t):
    key = int(input())
    doors = list(map(int, input().split()))
    
    seen_doors = 1
    while doors[key-1] != 0:
        key = doors[key-1]
        seen_doors += 1
    
    if seen_doors == 3 : # 3 doors opened
        print("YES")
    else :
        print("NO")
        
    