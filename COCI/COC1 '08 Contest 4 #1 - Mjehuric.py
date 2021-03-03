'''COC1 '08 Contest 4 #1 - Mjehuric'''

# take 5 numbers from the user and store it in a list
n = list(map(int, input().split()))[:5]

for i in range(5): 
    # check for numbers beside the current num index
    # ie. i = 1, then second loop will loop 4 times because there are 4 indexes left
    # ie. i = 4, then second loop will loop once bececause there is 1 index left
    for j in range(0, 5 - i - 1): 
        if n[j] > n[j + 1]: # check if the left number is greater than the right number
            n[j], n[j + 1] = n[j + 1], n[j] # if yes, swap them

            print(*n, sep = " ") # print the array without brackets, separate by space
