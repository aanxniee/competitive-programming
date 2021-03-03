'''CCC '08 J4 - From Prefix to Postfix'''

s = input() # prefix notation

while s != '0':

    s = list(s.split())[::-1] # split the string into a list and reverse it

    stk = []                
    x = ['+', '-'] # operators

    for ch in s: # iterate through the prefix notation 
        # if the character is an operator, remove top two items of the stack
        if ch in x: 
            a = stk.pop()
            b = stk.pop()

            # move the operator to after the two numbers
            stk.append(a + " " + b + " " + ch)

        else:
            stk.append(ch)

    res = stk[0].split()
    print(*res, sep = " ")
    
    s = input()