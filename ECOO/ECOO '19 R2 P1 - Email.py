'''ECOO '19 R2 P1 - Email'''

for i in range(10): # 10 data sets
  
    arr = [] # array to store the emails
    N = int(input())  
    for j in range(N):
        arr.append(input().lower())

    ind = 0 # index
    arr2 = [] # array to store revised emails

    for email in arr: # iterate through every email to revise/validate it

        new = '' # revised emails
        
        for k in range(len(email)):
            if email[k] == '@': # find the index where the @ is located
                ind = k

        for l in range(ind): 
            if email[l] == '.': # . before @ sign is ignored
                continue
            elif email[l] == '+': # + and following characters are ignored
                break
            else:
                new += email[l] # add valid characters to the new email

        for m in range(ind, len(email)):
            new += email[m] # add every character after the @

        arr2.append(new) # append each revised email to the list

    print(len(set(arr2))) # find the number of dinstinct emails using set()