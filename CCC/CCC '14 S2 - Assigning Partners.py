'''CCC '14 S2 - Assigning Partners'''

n = int(input()) # number of students
a = list(input().split()) # list of names 
b = list(input().split()) # list of their partners

i = 0
ans = 'good'

# loop through the list to check if the two lists are arranged consistently
while ans == 'good' and n > i:
    pos = a.index(b[i]) # get the index of each name

    # if pos == i, they are partnered with themselves
    if a[i] != b[pos] or pos == i:
        ans = 'bad'
    
    i += 1

print(ans)