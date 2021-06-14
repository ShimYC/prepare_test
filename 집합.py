import sys
M=int(input())
data_set:set=set()
for i in range(M):
    data=sys.stdin.readline().split() #['명령','숫자']
    if data[0]=='add' and int(data[1]) not in data_set:
        data_set=data_set|{int(data[1])}
    elif data[0]=='remove' and int(data[1]) in data_set:
        data_set=data_set-{int(data[1])}
    elif data[0]=='check':
        if int(data[1]) in data_set:
            print(1)
        else:
            print(0)
    elif data[0]=='toggle':
        if int(data[1]) in data_set:
            data_set=data_set-{int(data[1])}
        else:
            data_set=data_set|{int(data[1])}
    elif data[0]=='all':
        data_set={i for i in range(1,21)}
    elif data[0]=='empty':
        data_set=set()