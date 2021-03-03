'''DWITE '07 R2 #4 - All is Balanced'''

# function to find if the string is balanced or not
def balanced(s):
    stack = []

    # iterate through the word
    for i in range(len(s)):
        # for every opening bracket, add closing one to the stack
        if s[i] == '(': 
            stack.append(')')
        elif s[i] == '{':
            stack.append('}')
        elif s[i] == '[':
            stack.append(']')

        # for every closing bracket, check if it matches with the top item of stack
        # opening and closing brackets have to be in order
        elif s[i] == ')' or s[i] == '}' or s[i] == ']':
            if len(stack) > 0:
                if stack[-1] != s[i]: # if not, break
                    break

                else:
                    stack.pop(-1) # otherwise, remove from stack

    # if all brackets have been matched (stack is empty), it is balanced
    if len(stack) == 0: 
        return 'balanced'
    else:
        return 'not balanced'
        
for i in range(5):
    s = input()

    print(balanced(s))