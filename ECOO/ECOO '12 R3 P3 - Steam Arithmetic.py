'''ECOO '12 R3 P3 - Steam Arithmetic'''

# acceptable operators
OPERATORS = ['+', '-', '*', 'q', 'r']

# function to evaluate the steam arithmetic
def evaluate(s):
    stk = []
    
    # iterate through the steam arithmetic 
    for i in range(len(s)):
        # if the character is not an operator, add it to the stack
        if s[i] not in OPERATORS:
            stk.append(int(s[i]))

        else: # otherwise, pop the top two numbers from the stack
            a = stk.pop()
            b = stk.pop()

            if s[i] == '+':
                stk.append(a + b) 
            elif s[i] == '-':
                stk.append(a - b) 
            elif s[i] == '*':
                stk.append(a * b)

            elif s[i] == 'q':
                # make sure you don't get a case of division by 0
                if a > 0 and b < 0 or a < 0 and b > 0 and a % b != 0:
                    stk.append(a // b + 1)

                else:
                    stk.append(a // b)
                    
            elif s[i] == 'r':
                stk.append(a % b)

    return stk.pop()

for i in range(10):
    # split the steam arithmetic expression into a list
    exp = list(input().replace('(', "").replace(')', "").split())

    print(evaluate(exp[::-1])) # pass the reversed expression into the function