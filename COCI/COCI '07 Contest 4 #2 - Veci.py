'''COCI '07 Contest 4 #2 - Veci'''

n = int(input())
# separate the number by digits and put it into a list
# ie. [6, 5, 2, 9, 7, 1]
n = [int(x) for x in str(n)]

# iterate from the back of the list and find a digit (a) that is smaller than
# the previous digit
# ie. i = 3 n[i] = 9
for i in range(len(n) - 1, 0, -1):
    if n[i] > n[i - 1]:
        break

# if you reach the beginning of the list and no digit was found, there are no answers
if i == 1 and n[i] <= n[i - 1]:
    print(0)

else:
    a = n[i - 1] # digit that is smaller than the previous digit, ie. a = 2
    smallest = i # index of the digit that is next to a, ie. smallest = 3

    # search the right side of a to find the smallest number greater than a
    for j in range(i + 1, len(n)):
        if n[j] > a and n[j] < n[smallest]:
            smallest = j # smallest = 4

    # swap the two values, ie. [6, 5, 7, 9, 2, 1]
    n[i - 1], n[smallest] = n[smallest], n[i - 1]

    b = n[:i] # ie. [6, 5, 7]
    c = sorted(n[i:]) # sort the list starting from the digit after a, ie. [1, 2, 9]

    print(*b + c, sep = '') # ie. 657129