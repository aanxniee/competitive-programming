'''CCC '18 J2 - Occupy Parking'''

n = int(input())
y = list(input()) # yesterday's parking lot
t = list(input()) # today's parking lot

c = 0 # count of occupied spaces

for i in range(n):
    if y[i] == 'C' and t[i] == 'C': # check if they're occupied in both days
        c += 1

print(c)




