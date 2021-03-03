'''CCC '16 S2 - Tandem Bicycle'''

a = int(input()) # question 1 or 2
n = int(input()) # number of citzens from each city

d = list(map(int, input().split()))[:n] # dmojistan cyclers, ie. [5, 1, 4]
p = list(map(int, input().split()))[:n] # pegland cyclers, ie. [6, 2, 4]

# sort each list
d.sort() # [1, 4, 5]
p.sort() # [2, 4, 6]

t = 0 # total speed (sum of n individual bike speeds)

if a == 1: # question 1, minimum total speed
    # pair a biker from each city by least with least
    for i in range(n):
        # add the bike speed of each pair to the total
        # ie. total = 2 + 4 + 6 = 12
        t += max(d[i], p[i]) 
else:
    b = d + p # new list with cyclers from both cities. ie. [5, 1, 4, 6, 2, 4]
    b.sort() # sort it, ie. [1, 2, 4, 4, 5, 6]

    for i in range(1, n + 1): 
        # add the 3 max bike speeds to the total
        # ie. total = 6 + 5 + 4 = 15
        t += b[-i] 
          
print(t)