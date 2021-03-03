'''CCC '20 J2 - Epidemiology'''

p = int(input()) 
n = int(input()) # number of infected on day 0
r = int(input()) # spread rate per day
t = n # total number of infected
i = 0 # days

if r != 1:
    # continue as long as the infected people do not surpass p
    while t <= p: 
        i += 1 # increment day
        t += n * r ** i # find the increase in infected per day

    print(i)

else: print(p // n)

    
