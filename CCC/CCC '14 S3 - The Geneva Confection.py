'''CCC '14 S3 - The Geneva Confection'''

t = int(input()) # test cases
for i in range(t):
    b = [] # stack for branch
    m = [] # stack for mountain
    res = 'Y'

    n = int(input()) # number of carts
    for j in range(n):
        m.append(int(input())) # add each cart to the mountain stack

    # if the last cart is not 1, pop from mountain stack and append to branch stack 
    while m[len(m)-1] != 1: 
        b.append(m[len(m)-1])
        m.pop()

    m.pop() # otherwise, pop from mountain stack and add it straight to the lake

    i = 2

    # if neither mountain stack or branch stack are empty, check if they contain the next cart
    while len(m) > 0 or len(b) > 0:
        if len(m) > 0 and len(b) > 0: 
            # if it is in branch stack, pop it into the lake and look for the next cart
            if b[len(b)-1] == i: 
                b.pop()
                i += 1

            # if it is in mountain stack, pop it into the lake and look for the next cart
            elif m[len(m)-1] == i: 
                m.pop()
                i += 1
                
            else: # otherwise, pop it from mountain stack and move it into branch stack
                b.append(m[len(m)-1])
                m.pop()

        elif len(m) > 0: 
            if m[len(m)-1] == i: 
                m.pop()
                i += 1

            else:
                b.append(m[len(m)-1])
                m.pop()

        else: 
            if b[len(b)-1] == i:
                b.pop()
                i += 1
                
            else: # top item of both stacks are not the desired cart
                res = 'N'
                break

    print(res)