'''CCC '00 S1 - Slot Machines'''

n = int(input()) # number of quarters in the jar
m1 = int(input()) # number of times machine 1 has been played
m2 = int(input()) # number of times machine 2 has been played   
m3 = int(input()) # number of times machine 3 has been played

count = 0 # number of times she can play
while n > 0: # iterate until her jar is empty

    n -= 1 # decrement the quarter count each time she plays
    m1 += 1 # increment the number of times machine 1 has been played 
    count += 1 # increment the number of times she can play
    if m1 == 35: # pays 30 quarters every 35th time it is played
        n += 30
        m1 = 0

    if n == 0: 
        break
        
    n -= 1 
    m2 += 1 # increment the number of times machine 2 has been played
    count += 1
    if m2 == 100: # pays 60 quarters every 100th time it is played
        n += 60
        m2 = 0

    if n == 0:
        break

    n -= 1
    m3 += 1 # increment the number of times machine 3 has been played
    count += 1
    if m3 == 10: # plays 9 quarters every 10th time it is played
        n += 9
        m3 = 0

    if n == 0:
        break

print(f"Martha plays {count} times before going broke.")
