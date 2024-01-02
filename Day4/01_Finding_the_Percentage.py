'''
Question Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

Task:
    dictionary with key/value pair of name:[marks]
    Print average marks of student and show 2 decimal place.

Input:
    Line 1 -> integer value 'n'
    Next n lines -> name marks
    Last line -> name 

Output:
    Give average marks of the required name.

Approach:
    1. get the students marks in query_score
    2. using formatting of 2 decimal position, we do 
        sum(query_score)/len(query_score)
    
'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # code starts here
    query_score = student_marks[query_name]
    print("{0:.2f}".format(sum(query_score)/len(query_score)))