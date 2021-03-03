'''CCC '11 S2 - Multiple Choice'''

n = int(input())
t, s = [], [] # arrays for teacher answers and student answers
c = 0 # number of correct answers

for i in range(n): t.append(input())
for i in range(n): s.append(input())

# check if the teacher answers are the same as the student answers
for i in range(n):
    if t[i] == s[i]:
        c += 1

print(c)
