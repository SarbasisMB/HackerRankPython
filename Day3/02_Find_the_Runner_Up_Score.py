''' 
Task:
    Given 'n' scores
    Store in list and find runner-up

Input:
    Line 1 -> Input n
    Line 2 -> Array of n integers

Output:
    Print runner up -> The second maximum value.

My Approach:
    1. Taking input of n
    2. Entering n integers into set.
    As set doesnot allow duplicates.
    3. Remove the max value from the set.
    4. Now print the max value from the set.
'''
if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    arr.remove(max(arr))
    print(max(arr))