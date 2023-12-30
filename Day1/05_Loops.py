'''
Task:
    Read an integer 'n'
    For non-negative integers, print the square of i [i < n]
'''
if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        print(f"{i**2}")