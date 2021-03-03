'''VM7WC '16 #4 Silver - Test or Test Cases?'''

# function to find the permutations/combinations
def perm(a, s, l):
    if len(s) == l: # base case, permutation cannot be longer than l
        return
    
    for i in range(len(a)):
        for j in a[i]:
            s += j # add the next letter to the string 
            print(s)
            
            perm(a[i + 1:], s, l) # recursive call
            s = s[:-1]

n, l = map(int, input().split()) # n = number of restrictions, l = max length of word
a = [] # list of letters to use

for i in range(n):
    s = input().split() 
    a.append(s[1:]) # add all the letters to a list

for i in a[0]:
    print(i) # starting letter
    perm(a[1:], i, l)
