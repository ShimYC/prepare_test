from collections import deque
n,cost=map(int,input().split())
coin=deque([])
for i in range(n):
    coin.appendleft(int(input()))

# print(n,cost,coin)
count=0
for i in coin:
    count+=cost//i
    cost=cost%i
    if cost==0:
        break
print(count)
