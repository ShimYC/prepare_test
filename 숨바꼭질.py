import sys
from collections import deque
def sol():
    N,K=map(int,input().split())
    
    if N>K:
        print(N-K)
        return 
    
    dp=[sys.maxsize]*(100000+1)

    cnt=0
    dp[N]=cnt
    queue=deque()
    queue.append(N)
    while queue:
        
        cnt+=1
        for _ in range(len(queue)):

            location=queue.popleft()
            if location<K and 2*location<=100000 and cnt<dp[2*location]:
                dp[2*location]=cnt
                queue.append(2*location)
            if location<100000 and cnt<dp[location+1]:
                dp[location+1]=cnt
                queue.append(location+1)
            if location>1 and cnt<dp[location-1]:
                dp[location-1]=cnt
                queue.append(location-1)
        
    print(dp[K])

sol()