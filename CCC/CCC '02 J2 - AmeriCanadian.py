'''CCC '02 J2 - AmeriCanadian'''

while True:
    word = input() # take in words from user
    if word == 'quit!':
        break

    if len(word) > 4: # ensure the word has more than four letters
        for i in range(len(word)): # iterate through each letter and suffix is a consonant
            if word[len(word)-3] != "a" and word[len(word)-3] != "e"\
               and word[len(word)-3] != "i" and word[len(word)-3] != "o"\
               and word[len(word)-3] != "u" and word[len(word)-3] != "y"\
               and word[len(word)-2:len(word)] == "or": # check if word ends in 'or'
            
                print(word.replace("or", "our")) # replace 'or' with 'our'
                
                break

            else: # no need to change the spelling
                print(word)
                break
    else:
        print(word)