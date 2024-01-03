'''
Question Link: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

Task:
    Need to swap the cases in string
    Given string is
        sWap cASE
    The output will be
        SwAP Case
'''
def swap_case(s):
    '''
    # Approach 1
    new_s = ''
    for _ in s:
        if _.isupper():
            new_s = new_s + _.lower()
        elif _.islower():
            new_s = new_s + _.upper()
        else:
            new_s = new_s + _ 
    return new_s
    '''
    
    # Approach 2
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)