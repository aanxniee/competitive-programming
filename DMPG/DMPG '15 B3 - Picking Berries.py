'''DMPG '15 B3 - Picking Berries'''

# function to remove berries
def pickingBerries(s):

    # changes 'o' and '*' to whitespace
    s = s.replace('o', ' ') 
    s = s.replace('*', ' ')

    return s

# dimensions of the bush                   
w, h = input().split()
w, h = int(w), int(h)

lines = [] # array to store the lines of the bush
for i in range(h):
    lines.append(input())

count = 0 # number of edible berries
for line in lines: # iterate through the lines to find edible berries
    count += line.count('o')
    
    print(pickingBerries(line))

# print the number of edible berries
for i in range(count):
    print('o', end = '')