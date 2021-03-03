'''CCC '16 J3 - Hidden Palindrome'''

string = input()
x = 1 # minimum length of palindrome (single letters are palindromes)

for i in range(len(string) + 1): # iterate through each letter
    for j in range(i): # get each substring
        # check if substring is the same reversed
        if string[j:i] == string[j:i][::-1]:
            # if new substring > x, set x as new substring
            x = max(x, i - j) 
print(x)