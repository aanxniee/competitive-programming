'''DMOPC '14 Contest 8 P2 - Tides'''

valid = True
maxIndex, minIndex = 0, 0 # variable to store the index of the max/min
mx = 0 # variable to store the max value
mn = 100000 # variable to store the min value

n = int(input())
if 3 <= n <= 1000:

    data = list(map(int, input().split()))[:n]

    # iterate through the list and find the value and index of the min 
    for i in range(len(data)):
        if data[i] < mn:
            mn = data[i]
            minIndex = i

    # iterate through the list to find the value and index of the max 
    for i in range(len(data)):
        if data[i] > mx:
            mx = data[i]
            maxIndex = i

    # incorrect data if the max value occurs before the min value
    if minIndex == len(data) - 1 or maxIndex == 0 or maxIndex < minIndex:
        valid = False

    # checks if the numbers between the min and max value are strictly increasing
    for i in range(minIndex + 1, maxIndex + 1):
        if data[i - 1] > data[i]:
            valid = False
                
    if valid:
        print(mx - mn)
    else:
        print("unknown")

else:
    pass