'''Riolky's Mock CCC S1 - Word Bot'''

# i dont know
VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'q', 'r'\
              's', 't', 'v', 'w', 'x', 'y', 'z']

def longest(s):

    vc, cc = 0, 0

    for i in range(len(s)):
        if s[i] in VOWELS:
            vc += 1
        elif s[i] in CONSONANTS:
            
    '''c1, r1 = 0, 0
    for i in range(len(s)):
        if s[i] in VOWELS:
            c1 += 1
            
        else:
            r1 = max(r1, c1)
            c1 = 0

    c2, r2 = 0, 0
    for j in range(len(s)):
        if s[i] in CONSONANTS:
            c2 += 1
            
        else:
            r2 = max(r2, c2)
            c2 = 0
            
    return max(r1, c1), max(r2, c2)'''


n, c, v = map(int, input().split())
s = input().lower()

res = longest(s)
if res[0] < v or res[1] < c:
    print('YES')
else:
    print('NO')

