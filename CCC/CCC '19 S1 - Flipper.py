'''CCC '19 S1 - Flipper'''

g = [[1, 2], [3, 4]]
s = list(input()) # split every character

for i in s:
    if i == 'H': # horizontal flip, swap the values of row 1 and row 2
        g[0][0], g[1][0] = g[1][0], g[0][0]
        g[0][1], g[1][1] = g[1][1], g[0][1]

    elif i == 'V': # vertical flip, swap the values ov column 1 and column 2
        g[0][0], g[0][1] = g[0][1], g[0][0]
        g[1][0], g[1][1] = g[1][1], g[1][0]

for i in g:
    print(*i, sep = ' ')
        

