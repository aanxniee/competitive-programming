'''Lexicographically Least Substring'''

# function to find the least substring
def leastSubstring(s, n):
    x = s[:n] # ie. str = iloveprogramming, n = 4, x = ilov
    mn = x # minimum substring

    for i in range(n, len(s)):
        x = x[1:n] + s[i] # ie. x = love, x = ovep, x = vepr, x = epro...
        
        if x < mn: # if new x is less than minimum, set it as minimum
            mn = x

    return mn
    
string = input()
k = int(input())
print(leastSubstring(string, k))
