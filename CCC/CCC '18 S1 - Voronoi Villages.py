'''CCC '18 S1 - Voronoi Villages'''

n = int(input())
v, s = [], [] # village location, size of village

for i in range(n):
    v.append(int(input())) # ie. [5, 16, 0, 10, 4, 15]
    
v.sort() # sort the village, ie. [0, 4, 5, 10, 15, 16]

# find the size of every village except the leftmost and rightmost
for i in range(1, len(v) - 1):
    
    # size = difference between the village's left and right point
    # ie. size of village 15 is 2.5 ((15 - 10) / 2) + 0.5 ((16 - 15) / 2) = 3.0
    x = ((v[i] - v[i - 1]) / 2) + ((v[i + 1] - v[i]) / 2)
    s.append(x)

print(min(s)) # smallest village size


