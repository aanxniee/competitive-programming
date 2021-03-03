'''CCC '05 S1 - Snow Calls'''

phoneList = [] # array to store the phone numbers

t = int(input())
for i in range(t):
    phoneList.append(input())

# iterate through each number in the list
for number in phoneList:

    new = "" # converted phone number
    i = 0 # index of the current phone number

    # ensures that the extra letters/numbers are removed
    while len(new) < 12:

        if number[i] == "0":
            new += "0"     
        elif number[i] == "1":
            new += "1"    
        elif number[i] == "2" or number[i] == "A" or number[i] == "B" or number[i] == "C":
            new += "2"         
        elif number[i] == "3" or number[i] == "D" or number[i] == "E" or number[i] == "F":
            new += "3"       
        elif number[i] == "4" or number[i] == "G" or number[i] == "H" or number[i] == "I":
            new += "4"     
        elif number[i] == "5" or number[i] == "J" or number[i] == "K" or number[i] == "L":
            new += "5"     
        elif number[i] == "6" or number[i] == "M" or number[i] == "N" or number[i] == "O":
            new += "6"    
        elif number[i] == "7" or number[i] == "P" or number[i] == "Q" or number[i] == "R" or number[i] == "S":
            new += "7"    
        elif number[i] == "8" or number[i] == "T" or number[i] == "U" or number[i] == "V":
            new += "8"      
        elif number[i] == "9" or number[i] == "W" or number[i] == "X" or number[i] == "Y" or number[i] == "Z":
            new += "9"

        i += 1

        # add the "-" in the correct spaces (after index 2 and 6)
        if len(new) == 3 or len(new) == 7: 
            new += "-"
            
    print(new)