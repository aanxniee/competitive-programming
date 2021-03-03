'''Unique Elements'''

arr = [] # list to store the numbers

for i in range(int(input())):
    arr.append(int(input())) # add list to numbers

# find the number of unique numbers using set()
print(len(set(arr)))
