T=int(input())
for i in range(T):
    fibolist=[[1,0],[0,1]]
    N=int(input())
    if N==0:
        print(*fibolist[0])
    elif N==1:
        print(*fibolist[1])
    else:
        for j in range(2,N+1):
            fib=[fibolist[j-1][0]+fibolist[j-2][0],fibolist[j-1][1]+fibolist[j-2][1]]
            fibolist.append(fib)
        print(*fibolist[-1])
