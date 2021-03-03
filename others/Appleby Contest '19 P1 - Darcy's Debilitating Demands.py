'''Appleby Contest '19 P1 - Darcy's Debilitating Demands'''

t = int(input()) # number of test cases
if 1 <= t <= 100:
    
    for i in range(t):
        n = int(input()) # supposed sum of the three numbers
        a = int(input()) 
        b = int(input()) 
        c = int(input()) 

        z = c # third number
        if z > n:
            z = n # if third number is greater than sum, set it equal to sum (max it can be)
        y = n - z # second number
        if y > b: 
            y = b # if second number is greater than b, set it equal to b (max it can be)
        x = n - y - z # first number
        if x > a: 
            x = a # if first number is greater than a, set it equal to a (max it can be)
        
        # check if the three numbers add up to the sum
        if (x + y + z) != n:
            print("-1")
            
        else:
            print(x, y, z)
    
else:
    pass