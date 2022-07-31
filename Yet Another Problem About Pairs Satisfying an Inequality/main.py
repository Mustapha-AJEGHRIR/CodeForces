"""
You are given an array a1,a2,…an. Count the number of pairs of indices 1≤i,j≤n such that ai<i<aj<j.

Input
The first line contains an integer t (1≤t≤1000) — the number of test cases.

The first line of each test case contains an integer n (2≤n≤2⋅105) — the length of the array.

The second line of each test case contains n integers a1,a2,…,an (0≤ai≤109) — the elements of the array.

It is guaranteed that the sum of n across all test cases does not exceed 2⋅105.

Output
For each test case, output a single integer — the number of pairs of indices satisfying the condition in the statement.

Please note, that the answer for some test cases won't fit into 32-bit integer type, so you should use at least 64-bit integer type in your programming language (like long long for C++).
"""



def count_lower_than(numbers, number, start=0, end=None):
    """Binary search over the id in the numbers array that is lower than number.
    """
    left_id = start
    right_id = len(numbers) - 1 if end is None else end 
    # left = numbers[left_id]
    right = numbers[right_id][1]
    
    if right < number :
        return len(numbers)
    
    while left_id != right_id:
        mid = (left_id + right_id) // 2
        
        if numbers[mid][1] < number:
            left_id = mid + 1
        else:
            right_id = mid
    return left_id


t = int(input())

for case in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    
    zipped_numbers = zip(numbers, range(1, n+1))     # pairs of (a_i , i)
    
    filtered_numbers = list(filter(lambda x: x[0] < x[1], zipped_numbers))  # filter with condition a_i < i
    
    n_prime = len(filtered_numbers) 
    
    counter = 0
    for i in range(n_prime-1, -1, -1):
        a = filtered_numbers[i][0]
        counter += count_lower_than(filtered_numbers, a, end = i)
        
    print(counter)
    
    