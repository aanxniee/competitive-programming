'''CCC '15 J1 - Special Day'''

sm, sd = 2, 18 # special month and day

m = int(input())
d = int(input())

# check if the user input occurs before or after the special day and month
if m == sm:
    if d == sd: print('Special')
    elif d < sd: print('Before')
    else: print('After')
    
elif m < sm: print('Before')
else: print('After')
