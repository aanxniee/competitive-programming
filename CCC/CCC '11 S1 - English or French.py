'''CCC '11 S1 - English or French'''

wordList = [] # array to store lines

n = int(input())
for i in range(n):
    wordList.append(input())

s = 0 # number of s
t = 0 # number of t

for line in wordList: # iterate through every word in each line
    for ch in line: # iterate through every chracter in each word
        if ch == 's' or ch == 'S': 
            s += 1
        elif ch == 't' or ch == 'T':
            t += 1

if t > s:
    print("English")
else:
    print("French")