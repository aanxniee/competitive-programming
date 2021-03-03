'''CCC '17 S1 - Sum Game'''

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split())) # swifters scores
b = list(map(int, input().split())) # semaphores scores

s1, s2 = sum(a), sum(b) # the two teams total scores

for i in range(n, 0, -1):
    if s1 == s2: # check when the two teams scores are the same
        print(i)
        break
    else: # if they are not, check the day before
        s1 -= a.pop()
        s2 -= b.pop()

else: print(0)
