import sys
N=int(input())
a=list(map(int,sys.stdin.readline().split()))
a.sort()
n=int(input())
b=list(map(int,sys.stdin.readline().split()))
for i in range(n):
    start=0
    end=N-1
    
    while True:
        mid=(start+end)//2
        if b[i]==a[start] or b[i]==a[end]:
            print(1)
            break
        elif b[i]==a[mid]:
            print(1)
            break
        else:
            if b[i]>a[mid] and start!=mid:
                start=mid
            elif b[i]<a[mid] and end!=mid:
                end=mid
            else:
                print(0)
                break