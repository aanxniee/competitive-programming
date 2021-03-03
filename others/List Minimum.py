'''List Minimum'''

arr = [] # list to store numbers
n = int(input())
for i in range(n):
    ele = int(input()) # take input from user
    arr.append(ele) # add to list

# iterate through the entire list until it is empty
while len(arr) > 0: 
    x = min(arr) # find the minimum of the list
    print(x)
    arr.remove(x) # remove the minimum
