'''
Task
    Two integers, a and b.
    We need to show output of division (a/b) in two format.
    1. Integer format
    2. Float format
'''
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(f"{a//b}")
    print(f"{a/b}")