'''
Task:
    Given 3 integers -> x, y, z.
    Create all possible coordinates (i, j, k) such that (i+j+k)!=n.

My Approach:
    1. Take input from user
    2. Nested Loops for range of x, y, z.
    3. If (i+j+k)!=n
        then add (i,j,k) in list
    4. print list
'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    coordinates=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i+j+k != n):
                    coordinates.append([i, j, k])
    print(coordinates)