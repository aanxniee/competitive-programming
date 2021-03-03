'''Appleby Contest '19 P3 - A Recursion Problem'''

# function to evaluate the prefix notation
def evaluate(s):
    stk = []

    # check if the character is a number, if it is, push it to the stack
    for i in range(len(s)):
        if s[i] != '+':
            stk.append(int(s[i]))

        else:
            # find the sum of the top two elements of the stack
            stk.append(stk.pop() + stk.pop())
                
    return stk.pop() # return the top element (the answer)

# remove the brackets and split it into a list
exp = list(input().replace('(', "").replace(')', "").split())

# pass the reversed list into the function
print(evaluate(exp[::-1]))