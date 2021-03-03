'''DMOPC '15 Contest 3 P2 - Cheesecake Distribution'''

n = int(input()) # number of friends
c = list(map(int, input().split()))[:n] # number of slices each friend grabbed
s = sum(c) # total number of slices

# if the sum is not divisible by the number of slices, it can never be equally shared
if s % n != 0:
    print("Impossible")
    
else:
    # number of slices each person gets to be equal
    equal = s/n
    m = 0 # number of minutes it will take to redistribute the slices

    for i in range(len(c)):
        # ie. n = 3, c = [6, 1, 2], equal = 3
        if c[i] > equal:
            # ie. 6 - 3 = 3, now c[i] = 3  
            m += c[i] - equal

    print(int(m))