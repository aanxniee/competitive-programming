'''CCC '20 S1 - Surmising a Sprinter's Speed'''

n = int(input())
a, s = [], [] # nested list of times and distances, list of speeds

for i in range(n):
    a.append([int(x) for x in input().split()])

# sort the list based on times from least to greatest
a.sort(key = lambda x:x[0])

# find all the speeds
for i in range(n - 1):
    # a[i + 1][1] - a[i][1] is the delta distance
    # a[i + 1][0] - a[i][0] is the delta time
    # speed = absolute value of delta distance / delta time
    s.append(abs((a[i + 1][1] - a[i][1]) / (a[i + 1][0] - a[i][0])))

print(max(s))
