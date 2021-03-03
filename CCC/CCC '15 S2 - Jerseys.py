'''CCC '15 S2 - Jerseys'''

j = int(input()) # number of jerseys
a = int(input()) # number of athletes

ans = 0

# array of jersey sizes
# ie. ['M', 'S', 'S', 'L'], jersey #1 is M, jersey #2 is S, etc
jersey = [input() for i in range(j)] 

for i in range(a):
    size, num = input().split() 

    # check if the jersey with the requested number has a equal/greater size
    # than requested (L < M < S, ascii values)
    if jersey[int(num) - 1] <= size:
        ans += 1
        jersey[int(num) - 1] = 'x' # mark that jersey as unavailable

print(ans)
