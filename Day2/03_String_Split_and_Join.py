'''
    This is a program to split the given string.
    Then replace the space with '-'
'''


def split_and_join(line):
    # write your code here
    line=line.replace(' ','-')
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)