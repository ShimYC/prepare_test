import sys
n,c=map(int,sys.stdin.readline().rstrip().split())
array=list(map(int,sys.stdin.readlines()))

array.sort()

start=0
end=1000000000
while True:
    count=0
    L=[]
    mid=(start+end)//2
    #print(start,mid,end)
    

    i=0
    j=1
    while j<=len(array)-1:
        if array[j]-array[i]>=mid:
            count+=1
            L.append((array[i],array[j]))
            i=j
            j=i+1
        else:
            j+=1
    if start==mid:
        break

    #print(f'count is {count}, L is {L}')
    if count<c-1:
        end=mid
    else:
        start=mid

print(min([b-a for a,b in L]))
