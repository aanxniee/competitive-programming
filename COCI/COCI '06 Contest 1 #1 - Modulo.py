'''COCI '06 Contest 1 #1 - Modulo'''

n = [] # list for the numbers
m = [] # list for the modulos of the numbers

for i in range(10):
    n.append(int(input()))

for i in range(10):
    m.append(n[i] % 42) # mod each number by 42

m.sort()

# find the distinct modulos
print(len(set(m)))