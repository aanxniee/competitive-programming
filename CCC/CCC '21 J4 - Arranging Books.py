'''CCC '21 J4 - Arranging Books'''

b = list(input())
c = 0
for i in range(len(b)):
    for j in range(0, len(b) - i - 1):
        if b[i] > b[i + 1]:
            b[i], b[i + 1] = b[i + 1], b[i]
            c += 1
print(c)
