'''CCCHK '08 J3 - Phonebook'''

from collections import Counter
from itertools import groupby

pb = {} # dictionary to store name : phone number

for i in range(int(input())):
    n, nb = input().split()
    pb[nb] = n # append each person and their number to the phonebook

dialed = [] # list to store the dialled numbers
for i in range(int(input())):
    dialed.append(int(input()))

# find the most commonly dialled number (mode) and store it in a list
a = groupby(Counter(dialed).most_common(), lambda x:x[1])
b = [val for val, count in next(a)[1]]

fv = str(min(b)) # find the least number if there are multiple dialled numbers
print(pb[fv]) # print the name associated with the number