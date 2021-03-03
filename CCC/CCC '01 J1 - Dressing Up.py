'''CCC '01 J1 - Dressing Up'''

# function to print a bowtie
def bowTie(h):
    # increment by 2, each row has 2 more stars than the previous row
    for i in range(0, h, 2): 
        string = '*' * (i + 1) 
        string += ' ' * (2 *(h - i - 1))
        string += '*' *(i + 1)
        print(string)
    
    # decrement by 2, each row has 2 less stars than the previous row
    for i in range(h - 2, 0, -2):
        string = '*' * (i)
        string += ' ' * (2 * (h - i))
        string += '*' * (i)
        print(string)

height = int(input())
bowTie(height)
