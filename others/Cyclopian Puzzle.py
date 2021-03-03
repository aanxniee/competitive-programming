'''Cyclopian Puzzle'''

# function to print all the moves required
def hanoi(n, A, B, C):
    if n == 1: print(f'{A}{C}') # base case
    else: # recursive call
        hanoi(n - 1, A, C, B) 
        print(f'{A}{C}')
        hanoi(n - 1, B, A, C)

n = int(input()) # number of discs
hanoi(n, 'A', 'B', 'C')