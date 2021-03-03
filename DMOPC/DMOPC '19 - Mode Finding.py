'''DMOPC '19 - Mode Finding'''

from collections import Counter
from itertools import groupby

n = int(input()) # number of numbers
arr = list(map(int, input().split()))[:n] # store numbers in a list

c = groupby(Counter(arr).most_common(), lambda x:x[1]) # find all the modes
m = [val for val, count in next(c)[1]] # store the modes in a list
m.sort()
print(*m, sep = ' ')