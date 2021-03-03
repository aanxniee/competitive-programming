'''CCC '18 J3 - Are We There Yet?'''

d = list(map(int, input().split())) # distances adjacent cities, between i and i + 1

for i in range(5):
    for j in range(5):
        if i == j: print(0, end = ' ') # the city itself, distance = 0, ie. [0][0], [1][1], [2][2]...
        elif j > i: print(sum(d[i:j]), end = ' ')
        else: print(sum(d[j:i]), end = ' ')

    print()
        
