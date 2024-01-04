'''
Question Link: https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

Task:
    String  -> 'S'
    Width   -> 'w'
    Wrap string into paragraph of width 'w'.

Parameters:
    string      -> a long string
    max_width   -> integer 

Return:
    string -> string with newline caracters("\n") where the breaks should be.


'''
import textwrap

def wrap(string, max_width):
    '''
    # Method 1
    wrapper=textwrap.TextWrapper(width=max_width)   # This line creates instance of TextWrapper class, where the width specifies that the width will not exceed the max_width
    word_list=wrapper.wrap(text=string)     # Store the string in list format
    new_String=""
    for element in word_list:
        new_String=new_String+element+"\n"
    return new_String
    '''

    # Method 2
    return textwrap.fill(string, max_width)     # This will not create a list and will directly convert to String

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)