import sys
n=int(input()) # 1<=N<=1,000,000 
arr=list(map(int,sys.stdin.readline().split())) # 1<=Ai<=1,000,000

#가장 큰 Ai찾고 그다음 큰거 찾고 >>> 가장 작은거 찾으면 끝
ans=0
for i in range(n):
    cnt=0
    det=-1
    for j in arr[i:]:
        if j>det:
            cnt+=1
            det=j
            print('i',i,'cnt',cnt,'det',det)
    if ans<cnt:
        ans=cnt
    print(f'cnt :{cnt}')
print(f'ans: {ans}')



