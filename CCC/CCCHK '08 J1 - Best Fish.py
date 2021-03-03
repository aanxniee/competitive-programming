'''CCCHK '08 J1 - Best Fish'''

# function to determine who caught the best fish
def bestFish(a, b):

    # if casper's largest product is greater than natalie's, he wins
    if max(a) > max(b): 
        return "Casper"
    # if natalie's largest product is greater than casper's, she wins
    elif max(a) < max(b):
        return "Natalie"
    else: # else, they tie
        return "Tie"

a = [] # array to store casper's fish product (width x length)
b = [] # array to store natalie's fish product (width x length)

casper = int(input()) # number of fish casper caught
for i in range(casper):
    weight, length = input().split()
    size = int(weight) * int(length) # calculate the fish product
    a.append(size) # add it to the list

natalie = int(input()) # number of fish natalie caught
for i in range(natalie):
    weight, length = input().split() # calculate the fish product   
    size = int(weight)* int(length) # add it to the list
    b.append(size)

print(bestFish(a, b))