'''CCC '19 S2 - Pretty Average Primes'''

from math import sqrt

# function to determine whether numbers are prime or not
def p(n):
    if n == 2 or n == 3: return True # 2 and 3 are prime numbers
    # if it is divisble by 2 or less than 2 it is not a prime number
    if n % 2 == 0 or n < 2: return False

    # iterate from 3 to root of n, dividing by prime numbers
    # O(TNsqrt(N))
    for i in range(3, int(sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    N = int(input()) * 2 # number x 2 = sum of two numbers a and b
    # loop from 2 until 'N', a and b cannot be greater than 'N'
    for i in range(2, N // 2): 
        # check if they are prime
        if p(i) and p(N - i): # i is a, N - i is b (a + b = N)
            print(i, N - i)
            break