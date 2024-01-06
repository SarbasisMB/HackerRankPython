'''
Question Link: https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

Task:
    Given integer 'n'
    For i from 1 to n, Give output for:
    1. Decimal
    2. Octal
    3. Hexadecimal
    4. Binary
'''
def print_formatted(number):
    # your code goes here
    for i in range(1, number+1):
        '''
        Calculate number of digits in binary representation of "number". Determines width of each column in the output 
        '''
        space=len(bin(number)[2:])
        # print(space)
        '''
        {i:>{space}}    -> Decimal (right-aligned with minimum width of space)
        {i:>{space}o}    -> Octal (right-aligned with minimum width of space) 
        {i:>{space}X}    -> Hexadecimal (right-aligned with minimum width of space) 
        {i:>{space}b}    -> Binary (right-aligned with minimum width of space)
        '''
        print(f"{i:>{space}} {i:>{space}o} {i:>{space}X} {i:>{space}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)