'''CCC '11 S3 - Alice Through the Looking Glass'''

# create the 5 by 5 grid
grid = [[0]*5 for i in range(5)]

# mark the positions where the crystals show on the grid
grid[0][1], grid[0][2], grid[0][3], grid[1][2] = 1, 1, 1, 1

# function to determine whether a coordinate on the grid contains a crystal
def crystal(m, x, y):

    # adjust the grid to the magnification level using recursion
    if grid[y // pow(5, m - 1)][x // pow(5, m - 1)] or m > 1 and\
       grid[y // pow(5, m - 1) - 1][x // pow(5, m - 1)] and\
       crystal(m - 1, x % pow(5, m - 1), y % pow(5, m - 1)) == 'crystal':
        return 'crystal'

    return 'empty'
    
n = int(input()) # number of test cases
for i in range(n):
    m, x, y = map(int, input().split()) # magnification level, x position, y position
    print(crystal(m, x, y))