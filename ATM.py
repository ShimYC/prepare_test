N=int(input())
P=list(map(int,input().split()))
#print(N,P)
P.sort()
ans=0
time=0
for i in P:
    ans+=time+i
    time+=i
print(ans)