'''CCC '18 J1 - Telemarketer or Not'''
   
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# check if it matches the pattern of a telemarketer's number
if (a == 8 or a == 9) and (d == 8 or d == 9) and (b == c):
    print('ignore')
else: print('answer')


