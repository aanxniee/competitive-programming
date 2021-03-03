'''CCCHK '08 J2 - Lucky Number'''

# function to calculate the one digit representation
def luckyNumber(arr):
    for i in arr: # iterate through each number in the list
        # add each digit of the number to the total
        total = sum(int(digit) for digit in str(i))

        while total > 9: # repeat if the total is not a single digit
            total = sum(int(digit) for digit in str(total))

        print(total)
    
arr = [] # array to store the user's numbers

n = int(input())
for i in range(n):
    ele = int(input())
    arr.append(ele)

luckyNumber(arr)