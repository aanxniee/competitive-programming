'''CCC '06 S2 - Attack of the CipherTexts'''

pt = input() # plaintext message
ct1 = input() # ciphertext message that corresponds to plaintext
ct2 = input() # ciphertext message to decode
ans = '' # decoded message

# dictionary for mapping the letters 
letters = {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None,
           'G': None, 'H': None, 'I': None, 'J': None, 'K': None, 'L': None,
           'M': None, 'N': None, 'O': None, 'P': None, 'Q': None, 'R': None,
           'S': None, 'T': None, 'U': None, 'V': None, 'W': None, 'X': None,
           'Y': None, 'Z': None}

# iterate through the plaintext to map the letters (find the key)
for i in range(len(pt)):
    letters[ct1[i]] = pt[i]

for ch in ct2:
    if ch in ct1:
        ans += letters[ch]
    else:
        ans += '.'

print(ans)