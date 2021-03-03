'''Back to School '16 - Harambe'''

s = input()
x, y = 0, 0 # lower case count, upper case count

for ch in s: # iterate through every letter of the string
    if ch.islower(): # if the letter is lower case, increment lower case count
        x += 1
    elif ch.isupper(): # if the letter is upper case, increment upper case count
        y += 1

if x > y: # change to lower case if there is more lower case
    print(s.lower())
elif x < y: # change to upper case if there is more upper case 
    print(s.upper())
elif x == y:
    print(s)