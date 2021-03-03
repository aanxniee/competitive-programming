'''CCC '15 J2 - Happy or Sad'''

happy = 0 # number of happy faces
sad = 0 # number of sad faces
line = input()

if 1 <= len(line) <= 255:
    for i in range(len(line)): # iterate through every character in the line
        # check if there are happy faces :-) 
        if line[i] == ':' and line[i+1] == '-' and line[i+2] == ')':
            happy += 1

        # check if there are sad faces :-(
        elif line[i] == ':' and line[i+1] == '-' and line[i+2] == '(':
            sad += 1

if happy == 0 and sad == 0:
    print("none")
# if there are equal amounts of happy and sad faces, print none
elif happy == sad: 
    print("unsure")
elif happy > sad: # more happy faces
    print("happy")
else: # more sad faces
    print("sad")