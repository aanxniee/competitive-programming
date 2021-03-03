'''CCC '21 S2 - Modern Art'''

import sys
from collections import Counter

input = sys.stdin.readline

m = int(input())
n = int(input())

g = [['B'] * n for i in range(m)]

c = 0

k =  int(input())
arr = [input().split() for i in range(k)]

for ele in arr:
    if (arr.count(ele)) % 2 == 0:
        arr = list(filter((ele).__ne__, arr))
    else:
        arr = list(filter((ele).__ne__, arr))
        arr.append(ele)

for ele in arr:
    rc, num = ele[0], ele[1]
    
    if rc == 'R':
        for col in range(n):
            if g[int(num) - 1][col] == 'B': g[int(num) - 1][col] = 'G'
            else: g[int(num) - 1][col] = 'B'

    else:
        for row in range(m):
            if g[row][int(num) - 1] == 'B': g[row][int(num) - 1] = 'G'
            else: g[row][int(num) - 1] = 'B'
    
for i in range(m):
    for j in range(n):
        if g[i][j] == 'G':c += 1
            
print(c)
