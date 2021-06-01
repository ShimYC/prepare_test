import sys
n=int(input())
L=[]
ans=[]
for i in range(n):
    x,y=input().split()
    L.append((int(x),y,i))  # 정확한 정렬을 위해 x를 int형으로 바꿔주어야함
L.sort(key=lambda x:(x[0],x[2]))

for i in L:
    print(*i[:2])