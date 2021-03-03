'''DWITE '08 R3 #2 - Wordcount++'''

# function to split contracted words 
# ie. don't = don, t
def remove(line):

    for word in line:
        if "'" in word:
            copy = word.split("'") # splits by apostrphe   
            for x in copy: # add each split word into the list
                line.append(x)     
            line.remove(word) # remove the contracted word
    return line

def count(line):
    count = 0 # number of words in the line
    for word in line: 
        new  = '' # new line with valid words (length > 3, alphabetical)
    
        for ch in word: # check for alphabetical characters
            if ch.isalpha():
                new += ch

        if len(new) > 3: # check for length greater than 3
            count += 1
            
    print(count)

line1 = input().split()
line2 = input().split()
line3 = input().split()
line4 = input().split()
line5 = input().split()

count(remove(line1))
count(remove(line2))
count(remove(line3))
count(remove(line4))
count(remove(line5))
