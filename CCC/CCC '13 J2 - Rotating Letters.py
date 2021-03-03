'''CCC '13 J2 - Rotating Letters'''

valid = True
# possible letters that she can use (rotates by 180)
letters = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']
word = input()

if 1 <= len(word) <= 30:
    
    for ch in word: # iterate through each letter
        if ch in letters: # check if each letter is valid
            valid = True
        else:
            valid = False
            break

    if valid == True:
        print("YES")
    else:
        print("NO")

else:
    pass