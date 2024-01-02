'''
Question Link: https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true

Task:
    Given integer 'n'
    'n' values written in line, 
    create tuple 't' of those 'n' integers
    print the 'hash(t)'
'''
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))