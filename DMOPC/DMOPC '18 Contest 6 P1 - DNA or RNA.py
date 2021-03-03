'''DMOPC '18 Contest 6 P1 - DNA or RNA?'''

# list of possible molecules
molecule = ['A', 'C', 'G', 'T', 'U']

# function to see if the sequence is valid
def sequence(string):
    proper = False
    
    for ch in string:
        if ch in molecule:
            proper = True
        else:
            proper = False
            break
            
    # if both thymine and uracil are present, it is neither DNA or RNA
    if proper == True:
        if 'T' in string and 'U' in string:
            return 'neither'
        elif 'T' in string: # thymine is only found in DNA
            return "DNA"
        elif 'U' in string: # uracil is only found in RNA
            return "RNA"
        else: # if neither is found, it can be both
            return "both"
    else:
        return "neither"

n = int(input())
if 1 <= n <= 1000000:
    seq = input()
    if len(seq) > n:
        pass
    else:
        print(sequence(seq))
else:
    pass