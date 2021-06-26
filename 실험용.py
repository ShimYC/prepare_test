import heapq
from collections import deque
L=[]
L2=[]
X=[1,2,100,3,2,100,101,3,3,2,2]
for a in X:
    heapq.heappush(L,a)
    heapq.heappush(L2,-a)

print(L)
print(L2)

# print(heapq.heappop(L))

for i in range(len(L)):
    print('******************')
    print(heapq.heappop(L))
    print(L)
    print('******************')
    print(-heapq.heappop(L2))
    print(L2)

a=deque([2,2,3,3])
print(list(a)[:2])
b=deque([4,5,6])
c=deque(list(a)[:2])+deque([3])+deque(list(b)[1:])
print(c)