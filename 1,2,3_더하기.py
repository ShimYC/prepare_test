import sys
T=int(input())

for _ in range(T):
    n=int(sys.stdin.readline().rstrip())
    dp=[0,1,2,4,7]

    if n<=4:
        print(dp[n])
        continue

    dp=dp+[0]*(n-4)
    for i in range(5,n+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[-1])