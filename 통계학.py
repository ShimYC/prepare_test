import sys
N=int(input())
C_list=[0 for _ in range(8001)]
for _ in range(N):
    num=int(sys.stdin.readline().rstrip())
    C_list[num+4000]+=1
temp=max(C_list)
temp_list=[]
for i in range(8001):
    if C_list[i]==temp:
        temp_list.append(i-4000)
if len(temp_list)==1:
    many=temp_list[0]
else:
    many=temp_list[1]
Newlist=[]

for i in range(8001):
    if C_list[i]!=0:
        for j in range(C_list[i]):
            Newlist.append(i-4000)

mean=sum(Newlist)/N
mid=Newlist[N//2]
_range=Newlist[-1]-Newlist[0]
print(round(mean))
print(mid)
print(many)
print(_range)