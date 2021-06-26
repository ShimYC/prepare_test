# 예시 사례를 dp테이블로 N=6정도 까지 확인해보면 피보나치 규칙임을 알 수 있다.

N=int(input())
def sol(N):
    if N==1 or N==2:
        return N
    L=[0]*(N+1)
    
    L[1]=1
    L[2]=2
    

    for i in range(3,N+1):
        L[i]=(L[i-1]+L[i-2])%15746
    return L[N]
    
print(sol(N))