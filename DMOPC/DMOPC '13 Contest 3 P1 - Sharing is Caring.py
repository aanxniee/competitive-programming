'''DMOPC '13 Contest 3 P1 - Sharing is Caring'''

n, m = input().split() # n = number of people, m = number of documents
p, q, d = [], [], []

for i in range(int(m)):
    pi, qi = input().split()
    p.append(pi) # add the creator of the doc to the list
    q.append(qi) # add the shared people of the doc to the list
    d.append(input()) # name of the doc

y = input()

# if the p is not equal to your number (you didn't create the doc) and q is
# your number (shared with you), then you can see the doc
for i in range(int(m)):
    if q[i] == y:
        print(d[i])