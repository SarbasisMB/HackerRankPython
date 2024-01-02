'''
Question link: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

Task:
    list = []
    Perform the following
        1. insert i e: Insert integer  at position .
        2. print: Print the list.
        3. remove e: Delete the first occurrence of integer .
        4. append e: Insert integer  at the end of the list.
        5. sort: Sort the list.
        6. pop: Pop the last element from the list.
        7. reverse: Reverse the list.
'''
if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(0, N):
        command, *value = input().split()
        if command == 'insert':
            value = list(map(int, value))
            lst.insert((value[0]), value[1])
        elif command == 'print': 
            print(lst)
        elif command == 'remove': 
            lst.remove(int(value[0]))
        elif command == 'append': 
            lst.append(int(value[0]))
        elif command == 'sort': 
            lst.sort()
        elif command == 'pop': 
            lst.pop()
        else:
            lst.reverse()