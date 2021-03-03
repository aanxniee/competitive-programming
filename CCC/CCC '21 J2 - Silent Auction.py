'''CCC '21 J2 - Silent Auction'''

n = int(input())
name, bid = [], []

for i in range(n):
    name.append(input())
    bid.append(int(input()))

mx = bid.index(max(bid))

print(name[mx])
    
