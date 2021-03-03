'''CCC '21 S3 - Lunch Concert'''

import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n): a.append([int(x) for x in input().split()])

mx = 0

for i in range(n): if a[i][0] > mx: mx = a[i][0]

t = [0 for i in range(mx)]

for i in range(mx):
    for j in range(n):
        if abs(i - a[j][0]) > a[j][2]:
            t[i] += (abs(i - a[j][0]) - a[j][2]) * a[j][1]

print(min(t))
    

