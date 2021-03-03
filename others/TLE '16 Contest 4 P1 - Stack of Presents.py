'''TLE '16 Contest 4 P1 - Stack of Presents'''

import sys

p = [] # list of the present weights
n = int(sys.stdin.readline())

for i in range(n):
    p.append(int(sys.stdin.readline())) # ie. [7, 8, 2, 5, 10]
p.sort() # sort from least to most heavy, ie. [2, 5, 7, 8, 10]

w = p[0] # set the minimum weight (index 1 because the list is sorted), ie. w = 2
b = 1 # number of boxes

# iterate through the remaining weights
for i in range(1, len(p)):
    # if their weight is greater than the sum of weights, they can be stacked upon
    if w <= p[i]:
        # increment the sum weight
        # ie. 5 > 2 so w = 2 + 5 = 7, 7 = 7 so w = 7 + 7 = 14, 8 < 14, 10 < 14
        w += p[i]  
        b += 1 # incremenent the number of boxes

print(b)