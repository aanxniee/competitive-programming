'''CCC '19 J1 - Winning Score'''

a, b = 0, 0

# take in the scores of apples
for i in range(3, 0, -1): 
    a += int(input()) * i # find their total score

# take in the scores of bananas
for i in range(3, 0, -1):
    b += int(input()) * i # find their total score

if a > b: print('A')
elif a < b: print('B')
else: print('T')
