'''Postfix Notation'''

# acceptable operators
OPERATORS = ['*', '/', '+', '-', '%', '^']

p = list(input().split()) # postfix notation split into a list
stk = []

# iterate through the postfix expression and check if the character is an
# operator or operand
for i in range(len(p)):
    
    # if it is an operand, push to stack
    if p[i] not in OPERATORS:
        stk.append(p[i])
        
    # if it is an operator, pop the top to elements of the stack
    else: 
        a = stk.pop()
        b = stk.pop()

        # concatenate a string by placing the operator between the two operands
        if p[i] == '^':
            stk.append('(' + b + '**' + a + ')') # fix the operator for exponential
        else:
            stk.append('(' + b + p[i] + a + ')')

# evaluate the final string
if len(stk) == 1:
    print(eval(stk[0]))