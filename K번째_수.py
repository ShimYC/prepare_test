import sys
n,k=map(int,sys.stdin.readlines())

#N개 배열에서 S보다 작거나 같은 숫자의 개수

def lower_than_S(S:int,n:int) -> int: #함수를 정의할 때, 변수 타입을 명시하는 습관 들이기.
    return sum([min(S//i,n) for i in range(1,n+1)])

#이분탐색
start:int=1
end:int=k
while start<=end:
    mid=(start+end)//2
    print(start,mid,end)
    temp:int=lower_than_S(mid,n)
    if temp>=k:
        end=mid-1
    else:
        start=mid+1
print(start,mid,end)
#정답 출력
print(start)

#왜 mid가 아니라 start이어야 하는가?