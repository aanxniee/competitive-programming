'''CCC '17 S2 - High Tide, Low Tide'''

n = int(input())
half = n // 2 # halfway point

t = sorted(list(map(int, input().split()))) # sorted tide measurements

if n % 2 == 0: # even number of measurements, same number of low and high tides
    # use the halfway point to find the low and high measurements
    low, high = t[:half][::-1], t[half:] 
    
    for i in range(half):
        print(low[i], high[i], end = ' ') # alternate between low and high 

else: # odd number of measurements, start with low tide and end with low tide
    x = t.pop(0) # lowest tide, temporarily remove from list
    # use the halfway point to find the low and high measurements
    low, high = t[:half][::-1], t[half:]

    for i in range(half):
        print(low[i], high[i], end = ' ')
    print(x) # include the lowest tide at the end
