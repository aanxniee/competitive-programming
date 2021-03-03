'''Interleaving Leaves'''

for i in range(int(input())):
    n = int(input()) # number of leaves in each pile
    a, b = input()[::-1], input()[::-1] # reverse each pile

    p = '' # final pile

    for j in range(n):
        p += b[j] # add one leaf from pile 2
        p += a[j] # followed by one leaf from pile 1, repeat

    print(p)
