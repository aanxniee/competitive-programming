'''CCC '20 J1 - Dog Treats'''

s = int(input())
m = int(input())
l = int(input())

# calculate happiness using formula
t = s + 2 * m + 3 * l

if t >= 10:
    print("happy")
else:
    print("sad")
