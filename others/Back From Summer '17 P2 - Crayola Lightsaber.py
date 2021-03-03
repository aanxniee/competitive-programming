'''Back From Summer '17 P2 - Crayola Lightsaber'''

from collections import Counter

n = int(input()) # number of colours
c = list(input().split())[:n] # colours of markers

x = Counter(c) # count the occurence of each colour of marker
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'black']
count = []

# map each colour to the number of markers it has
for i in colours:
    count.append(x[i])

mx = max(count) # colour with the greatest amount of markers
r = n - mx # remaining markers (total number - max amount)

print(min(mx, r + 1) + r)