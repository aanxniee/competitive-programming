'''CCC '13 S1 - From 1987 to 2013'''

# function to find if the year has all distinct digits
def uniqueYear(a):
    arr = [] # list to store digits
    for i in range(len(a)): # iterate through the digits of the year
        if a[i] in arr: # if digit is already in list, it is repeated
            break
        else:
            arr.append(a[i]) # otherwise, add it to the list

    if len(arr) == len(a): # if no digits are repeated, it is unique
        return True
    else:
        return False

d = int(input()) 

if uniqueYear(str(d)): 
    d += 1 # ie. 1987 --> 1988

# keep increasing the year until you find the next unique year
while not uniqueYear(str(d)):
    d += 1

print(d)