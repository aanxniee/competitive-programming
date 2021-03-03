'''CCC '20 J3 - Art'''

n = int(input())
x, y = [], [] # lists to store x and y coordinates

for i in range(n):
    a, b = input().split(',')
    x.append(int(a))
    y.append(int(b))

bx, by = min(x) - 1, min(y) - 1 # bottom-left corner (lowest point, min)
tx, ty = max(x) + 1, max(y) + 1 # top-right corner (uppermost point, max)

print(f'{bx},{by}')
print(f'{tx},{ty}')


