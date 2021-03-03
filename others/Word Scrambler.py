'''Word Scrambler'''

from itertools import permutations

s = input() 
x = [] # list for permutations

# function to find permutations
def words(a):
    for i in range(1, len(a) + 1):
        yield from map(''.join, permutations(a, i))

# take all permutations that are the length
for i in words(s):
    if len(i) == len(s):
        x.append(i)

x.sort() # sort alphabetically
for i in x:
    print(i)