'''CCC '16 S1 - Ragaman'''

# turn the user's input into a list of letters
str1 = [x for x in input()]
str2 = [x for x in input()]

# copy the first string
temp = [x for x in str1]

# iterate through the copy and check if each letter is in string 2
for i in temp:
    if i in str2:
        # remove the letter from both lists (string)
        str1.remove(i)
        str2.remove(i)

# check if count of astericks is the same as the letters remaining
# each letter should have an asterick
if len(str1) == str2.count('*'):
    print('A')
else:
    print('N')