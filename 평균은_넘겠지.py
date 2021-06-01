'''
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

둘째 줄부터 각 테스트 케이스마다 학생의 수 
N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 
이어서 N명의 점수가 주어진다. 
점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 
반올림하여 소수점 셋째 자리까지 출력한다.
'''
import sys
test_case=int(input())

for i in range(test_case):
    data=list(map(int,sys.stdin.readline().split()))
    count=0
    average=sum(data[1:])/data[0]
    for j in range(1,data[0]+1):
        if data[j]>average:
            count+=1
    answer=round(count/data[0]*100,3)
    print(f'{answer:.3f}%' )