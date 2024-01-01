'''
Task:
    Name, Grade of N students.
    Print second lowest grade

Input:
    Line 1 -> Total cases
    Line 2 -> Name, Score pair inputs of total cases

Output:
    Print names with 2nd lowest grades

Approach:
    1. Create 2 list, i. for storing pairwise of name, score, ii. for storing scores
    2. convert the Score list into set, so that all the duplicates get deleted. Then sort the set, and store the element of position 1 into variable 'check'
    3. Using filter, we will filter out the required pairs required.
    Here we have "filter(lambda x: x[1]==check, pair_lst)"
    This will filter the pair_list based on the 'check' value.
    Convert this filtered pair in list.
    4. Sort the name list
    5. using loop print the name of the students
'''
if __name__ == '__main__':
    pair_lst=[]
    score_lst=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        pair_lst.append([name, score])
        score_lst.append(score)
    check=sorted(set(score_lst))[1]
    name_lst=list(filter(lambda x: x[1]==check, pair_lst))
    name_lst.sort()
    for _ in name_lst:
        print(_[0])