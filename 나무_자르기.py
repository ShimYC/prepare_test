import sys
from collections import Counter
n,m= map(int,input().split())
trees=Counter(map(int,sys.stdin.readline().split()))
start,end = 0,max(trees)
print(trees)
print(trees.items())
while(start<=end):
    count=0
    mid=(start+end)//2
    
    count=sum([(i-mid)*cnt for i,cnt in trees.items() if i>mid])        
    if count<m:
        end=mid-1
    else:
        result=mid
        start=mid+1
print(result)
