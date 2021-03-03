'''CCC '05 J5 - Bananas'''

# function to convert normal words into monkey words
def monkey(s):
    while 'ANA' in s or 'BAS' in s:
        s = s.replace('ANA', 'A')
        s = s.replace('BAS', 'A')

    # if the normal word can be reduced to 'A', it is a monkey word
    if s == 'A': return True
    else: return False

s = input()
while s != 'X':
    
    if monkey(s): print('YES')
    else: print('NO')

    s = input()