'''CCC '19 J3 - Cold Compress'''

from itertools import groupby

n = int(input())
for i in range(n):
    s = input()
    
    g = groupby(s) # group every character with its count
    r = [(label, sum(1 for _ in group)) for label, group in g] # ie. ("T", 3)

    # format by count character, ie. 3 T
    print(" ".join("{} {}".format(count, label) for label, count in r))
