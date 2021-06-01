n=int(input())
road=list(map(int,input().split()))
cost=list(map(int,input().split()))
ans=0
#print('\n\n\n')
min_cost=cost[0]
stop_point=[0]
for i in range(1,len(cost)):
    #print(ans,min_cost,road[i-1])
    ans+=min_cost*road[i-1]
    if cost[i]<min_cost:
        min_cost=cost[i]
print(ans)


