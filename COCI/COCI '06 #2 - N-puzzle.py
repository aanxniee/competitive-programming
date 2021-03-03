'''COCI '06 Contest 3 #2 N-puzzle'''

p = [] # list to store the letters

for i in range(4):
    p.append(input())

s = 0 # scatter of the puzzle

# iterate through each letter
for r in range(4):
    for c in range(4):
        if p[r][c] == ".":
            continue
        
        else:
            # find the desired position of each letter
            dis = ord(p[r][c]) - ord('A')
            row, col = dis // 4, dis % 4

            # calculate the manhattan distance
            s += abs(r - row) + abs(c - col)

print(s)