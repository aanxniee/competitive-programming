'''Mock CCC '18 Contest 2 J3/S1 - An Array Problem'''

s, b = 0, 0 # sum, max value

for i in range(int(input())):
    a = int(input())
    s += a # add number to the sum
    b = max(a, b) # find the max value

print(min(s - b, s // 2)) # simultaneously decrease the largest and smallest element