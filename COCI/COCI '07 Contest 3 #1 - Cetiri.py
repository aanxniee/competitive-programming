'''COCI '07 Contest 3 #1 - Cetiri'''

 # take number from user and put into a list
a = list(map(int, input().split()))
a.sort() # sort the list, ie. [10, 1, 7] = [1, 7, 10]
p = 0 # difference between the numbers (rate of change)

if a[1] - a[0] < a[2] - a[1]:
    p = a[1] - a[0] 
    print(a[1] + p) # number fits between 2 and 3, becomes index 3
    
elif a[1] - a[0] > a[2] - a[1]:
    p = a[2] - a[1]
    print(a[0] + p) # number fits between 1 and 2, becomes index 2
    
elif a[1] - a[0] == a[2] - a[1]:
    p = a[2] - a[1]
    print(a[2] + p) # number is after 3, becomes index 4