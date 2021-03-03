'''CCC '07 J4 - Anagram Checker'''

string1 = list(input().strip())
string2 = list(input().strip())

for ch in string1: # remove whitespace in line 1
    if ch == ' ':
        string1.remove(ch)

for ch in string2: # remove white space in line 2
    if ch == ' ':
        string2.remove(ch)

# sort both lists alphabetically
string1.sort()
string2.sort()

# if lists are same, they are anagrams
if string1 == string2:
    print("Is an anagram.")
else:
    print("Is not an anagram.")
