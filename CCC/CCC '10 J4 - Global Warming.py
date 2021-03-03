'''CCC '10 J4 - Global Warming'''

while True:
    n = list(map(int, input().split()))
    
    if len(n) == 1 and n[0] == 0:
        break

    d = [] # list of differences

    # iterate through the numbers and find the difference by substracting next value by current value
    for i in range(1, len(n) - 1):
        d.append(n[i + 1] - n[i])

    pattern = True
    a = len(d) 

    # loop until you find the length of the pattern
    for i in range(1, len(d)):
        pattern = True
        for j in range(len(d)):
            if i + j < len(d) and d[j] != d[i + j]:
                pattern = False
                break

        if pattern:
            a = i
            break

    print(a)