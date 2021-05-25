from timeit import default_timer as timer
from datetime import timedelta

def fibonacci(n):
    n=int(n)
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
before_time=0
after_time=0
for i in range(40):
    start = timer()
    print(f'{i}번째 값:',fibonacci(i))
    end = timer()
    print('계산 소요시간:',timedelta(seconds=end-start))
    before_time=after_time
    after_time=end-start

    if before_time!=0:
        print(f'계산 소요시간 증가율은 대략: {after_time/before_time:.2f}')

# 재귀함수로 단순 코딩한 경우 대체로 1.5~1.7 사이의 계산 시간 증가율을 가짐
    