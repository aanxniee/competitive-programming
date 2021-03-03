'''CCC '18 S2 - Sunflowers'''

# no clue how this code works, daniel did it for me lol goated

def rearrange(n, arr):
    if arr[0][0] < arr[0][1] and arr[0][0] < arr[1][0]:
        for i in arr:
            for j in i:
                print(j, end = " ")
            print()
            
    elif arr[1][0] > arr[0][0] > arr[0][1]:
        for i in range(n):
            for j in range(n):
                print(arr[j][-i - 1], end = " ")
            print()
            
    elif arr[1][0] < arr[0][0] < arr[0][1]:
        for i in range(n):
            for j in range(n):
                print(arr[-j - 1][i], end = " ")
            print()

    else:
        for i in range(n):
            for j in range(n):
                print(arr[-i - 1][-j - 1], end = " ")
            print()
    
data = []

n = int(input())
if 2 <= n <= 100:
    for i in range(n):
        data.append(list(map(int, input().split())))

    rearrange(n, data)
    
else:
    pass