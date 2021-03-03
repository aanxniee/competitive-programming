'''CCC '21 S1 - Crazy Fencing'''

n = int(input())
a = 0

h = list(map(int, input().split()))
w = list(map(int, input().split()))

for i in range(n):
    a += ((h[i] + h[i + 1]) / 2) * w[i]

print(a)
                            
