'''CCC '13 J4 - Time on Task'''

t = int(input()) # number of minutes available to complete the chores
c = int(input()) # total number of chores to choose from
a = [] # list to store the minutes it takes to do each chore

for i in range(c):
    a.append(int(input())) # ie. [5, 4, 3, 2, 1]

a.sort() # [1, 2, 3, 4, 5]

n = 0 # number of chores that can be done

for i in range(len(a)): 
    if a[i] <= t: 
        t -= a[i] # decrement the time left
        n += 1 # increment number of chores done

print(n)