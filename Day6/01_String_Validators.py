'''
Question link: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

Task:
    1. str.isalnum() -> Alphabet + Numeric
    2. str.isalpha() -> Alphabet
    3. str.isdigit() -> Digit
    4. str.islower() -> Lowercase characters
    5. str.isupper() -> Uppercase characters

Input:
    String 'S'

Output:
    Result of AlphaNumeric characters
    Result of Alphabet characters
    Result of Numeric
    Result of Lowercase character
    Result of Uppercase characters
'''

if __name__ == '__main__':
    s = input()
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))