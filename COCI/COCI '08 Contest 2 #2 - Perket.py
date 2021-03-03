'''COCI '08 Contest 2 #3 - Perket'''

# i have no fucking clue tbh

# function to find the possible combinations of sourness/bitterness
def perm(p, s, b):
    global mn # smallest possible difference between sourness and bitterness
    
    if len(p) == 0: return # base case
    
    else:
        for i, c in enumerate(p):
            d = abs(s * c[0] - b - c[1])

            if mn > d: mn = d # reset value of minimum

            perm(p[i + 1:], s * c[0], b + c[1]) # recursive call
            
p = [] # list of sourness and bitterness
mn = 999999

for i in range(int(input())):
    p.append(list(map(int, input().split())))
    
perm(p, 1, 0)
print(mn)