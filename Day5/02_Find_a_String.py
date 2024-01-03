'''
Question Link: https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

Task:
    Input -> String, subString
    Output -> total occurrence of the subString in String

Input:
    ABCDCDC
    CDC
Output:
    2
'''
def count_substring(string, sub_string):
    '''
    # Approach 1 Failed max cases
    count=0
    for i in range(0, len(string)-2):
        if string[i:i+3] == sub_string:
            count = count + 1
    return count
    '''

    # Approach 2
    count=0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count=count+1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)