import sys
from collections import deque

L=[]
N=int(input())
for i in range(N):
    start,end=map(int,sys.stdin.readline().split())
    L.append((start,end))

L.sort()
L=deque(L)

start=0
New_list=[]
while True:
    if len(New_list)==0 or New_list[-1][1]==L[0][0] and L[0][0]==L[0][1]:
        New_list.append(L[0])
        L.popleft()
    elif L[0][1]<New_list[-1][1]:
        if len(New_list)<=1 or New_list[-2][1]<=L[0][0]:
            New_list.pop()
            New_list.append(L[0])
            L.popleft()
        else:
            L.popleft()
    elif L[0][0]>=New_list[-1][1]:
        New_list.append(L[0])
        L.popleft()
    else:
        L.popleft()
    if len(L)==0:
        break
#print(New_list)
print(len(New_list))