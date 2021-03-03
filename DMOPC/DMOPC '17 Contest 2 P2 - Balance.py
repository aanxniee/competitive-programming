'''DMOPC '17 Contest 2 P2 - Balance'''

# function to find if the string can be balanced
def balance(s):
    stack = []
    
    # iterate through the string
    for i in range(len(s)):
        # for every opening bracket, add a closing one to the stack
        if s[i] == '(':
            stack.append(')')
        
        # for every closing bracket, add an opening one if stack is empty 
        # or if the top item of the stack is not a closing bracket 
        elif s[i] == ')':

            if len(stack) == 0:
                stack.append('(')
            elif stack[-1] != s[i]:
                stack.append('(')   
            else: # otherwise, match the brackets and remove from stack
                stack.pop(-1)

    if len(stack) == 0: # all open brackets have a corresponding closing bracket
        return 'YES'
    elif len(stack) == 2: # one bracket can be inverted to match with the other bracket
        return 'YES'
    else:
        return 'NO'

s = input()
print(balance(s))