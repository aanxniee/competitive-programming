'''CCC '20 J4 - Cyclic Shifts'''

t = input()
s = input()

# function to find cyclic shifts, s = string, n = number of rotations
def shift(s, n):
    return s[n:] + s[:n] # slice the string, ie. HELLO with 1 rotation = ELLO + H 

a = [] # list of all possible shifts
for i in range(1, len(s) + 1):
    a.append(shift(s, i))

st = False

# iterate through the list and check if the elements are substrings of t
for ele in a:
    if ele in t:
        st = True
        break

if st: print('yes')
else: print('no')
    
    
    
