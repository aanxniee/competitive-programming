'''CCC '01 J2 - Mod Inverse'''

x = int(input())
m = int(input())
found = False

for n in range(101): # iterate from 1-100; m <= 100
    # ie. 4 x 17 = 52, 52 % 17 = 1
    if ((x * n) % m == 1):
        print(n)
        found = True
        break

if not found:
    print("No such integer exists.")
