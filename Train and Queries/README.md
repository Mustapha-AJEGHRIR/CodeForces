# Protected dicts
To understand the problem of hacking hashs in Python, take a look at this : https://codeforces.com/blog/entry/101817 . This link provides a way + explanation of counter hacks, for my case i just converted the int values into strings which is also a solution.
The problem is that the test case 5 contains a hash hack (will make your hashs for the lookup tables (py dict) very skew)