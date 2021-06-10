import sys
k,n=map(int,(input().split()))
line=list(map(int,sys.stdin.readlines()))
# print(k,n)
# print(line)
start=0
end=max(line)
while (start<=end):
    
    count=0
    mid=(start+end)//2
    if mid==0:
        mid=1
    #print(start,mid,end)
    for i in line:
        if i>=mid:
            count+=i//mid
    if count<n or mid>(2**31-1):
        end=mid-1
    else:
        result=mid
        start=mid+1
print(result)
    
