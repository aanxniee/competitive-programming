'''CCC '15 S1 - Zero That Out'''

arr = [] # array to store the numbers that the boss says

k = int(input()) # number of numbers the boss will say

for i in range(k):
    num = int(input())

    if num: # if it is a number not equal to 0, add to the list
        arr.append(num)
    else: # if the number is 0, pop the most recent number from the list
        arr.pop() 

print(sum(arr)) # find the sum of the numbers