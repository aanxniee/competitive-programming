'''CCC '10 S2 - Huffman Encoding'''

letters = [] # list to store the letters, ie. [A, B, C, D, E]
numbers = [] # list to store the corresponding numbers, ie. [00, 01, 10, 110, 111]

k = int(input())
for i in range(k):
    x, y = input().split()
    letters.append(x)
    numbers.append(y)

s = input() # string of numbers to decode, ie. 00000101111
new = '' # decoded string

while len(s) > 0: # iterate until given string is empty
    for i in range(k): 
        # check if it starts with numbers in the list, ie. 00...01...10...
        if s.startswith(numbers[i]):
            new += letters[i] # add the corresponding letter, ie. starts wit 00 = add 'A'
            s = s[len(numbers[i]):] # delete the segment we just decoded
            break
print(new)
