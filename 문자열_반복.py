import sys
n=int(input())
for i in range(n):
    a,b=input().split()
    ans=''
    for j in b:
        ans+=j*int(a)
    print(ans)