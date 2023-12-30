'''
Task    
    Given an integer.
    Perform the following task
    1. If 'n' is odd, print 'Weird'.
    2. If 'n' is even and in the inclusive range of 2 to 5, print 'Not Weird'.
    3. If 'n' is even and in the inclusive range of 6 and 20, print 'Weird'.
    4. If n is even and greater than 20, print 'Not Weird'.

'''
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if (n%2!=0) or (n%2==0 and (n>=6 and n<=20)):
        print("Weird")
    else:
        print("Not Weird")
