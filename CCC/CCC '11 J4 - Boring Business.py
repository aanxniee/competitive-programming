'''CCC '11 J4 - Boring Business'''

# create the grid using a dictionary and set all values within the grid as false
grid = {}
for row in range(-1, -400, -1):
    for col in range(-400, 400):
        grid[(row, col)] = False 

# identify the already drilled parts (danger) as true
grid[(-1, 0)], grid[(-2, 0)], grid[(-3, 0)], grid[(-3, 1)] = True, True, True, True
grid[(-3, 2)], grid[(-3, 3)], grid[(-4, 3)], grid[(-5, 3)] = True, True, True, True
grid[(-5, 4)], grid[(-5, 5)], grid[(-4, 5)], grid[(-3, 5)] = True, True, True, True
grid[(-3, 6)], grid[(-3, 7)], grid[(-4, 7)], grid[(-5, 7)] = True, True, True, True
grid[(-6, 7)], grid[(-7, 7)], grid[(-7, 6)], grid[(-7, 5)] = True, True, True, True
grid[(-7, 4)], grid[(-7, 3)], grid[(-7, 2)], grid[(-7, 1)] = True, True, True, True
grid[(-7, 0)], grid[(-7, -1)], grid[(-6, -1)], grid[(-5, -1)] = True, True, True, True

safe = True
row, col = -5, -1 # starting position

while safe:
    dr, ds = input().split() # direction, distance
    ds = int(ds)
    dx, dy = 0, 0 # change in direction along x and y axis
    
    if dr == 'q': # quit
        break
    elif dr == 'l': # move to the left
        dx = -1
    elif dr == 'r': # move to the right
        dx = 1
    elif dr == 'd': # move down
        dy = -1
    elif dr == 'u': # move up
        dy = 1

    while ds > 0:
        row += dy # add the movement for the x axis
        col += dx # add the movement for the y axis

        # check if it intersects with an already drilled part in the grid
        if not grid[(row, col)]:
            grid[(row, col)] = True
        else:
            safe = False
            
        ds -= 1

    if safe:
        print(col, row, 'safe')
    else:
        print(col, row, 'DANGER')