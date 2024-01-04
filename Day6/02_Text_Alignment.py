'''
Question Link: https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true

Task:
    Text alignment is used to align text left, right and center.
    [Here width is taken 20]

    1. .ljust(width)
        This method returns a left aligned string of length width.
        Example: print('HackerRank'.ljust(20,'-'))
    
    2. .center(width)
        This method reutns a centered string of lendth width.
        Example: print('HackerRank'.center(20,'-'))

    3. .rjust(width)
        This method returns a reight aligned string of lendth width.
        Example: print 'HackerRank'.rjust(20,'-')
'''
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
