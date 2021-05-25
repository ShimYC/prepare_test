from timeit import default_timer as timer
from datetime import timedelta

def fibonacci(n):
    n=int(n)
    _list=[0,1]
    if n==0:
        return _list[0]
    elif n==1:
        return _list[1]
    else:
        for i in range(n-1):
            _list.append(_list[-1]+_list[-2]) 
            # 피보나치수의 규칙은 마지막 두 수를 더한 값이 새로운 값이 되는 것.
        
        return _list[n]


before_time=0
after_time=0


for i in range(400):
    start = timer()
    print(f'{i}번째 값:',fibonacci(i))
    end = timer()
    print('계산 소요시간:',timedelta(seconds=end-start))

    before_time=after_time
    after_time=end-start

    # if before_time!=0:
    #     print(f'계산 소요시간 증가율은 대략: {after_time/before_time:.2f}')