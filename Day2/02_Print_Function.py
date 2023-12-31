'''
    Take input n
    Give output number in series

    If input : 3
    Output : 123
'''
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end='')