def move(n,a,b,c,_list:list):
    if n==1:
        _list.append((a,b))
    else:
        move(n-1,a,c,b,_list)
        _list.append((a,b))
        move(n-1,c,b,a,_list)
    return None


def hanoi(n):
    _list=[]
    move(n,1,3,2,_list)
    print(len(_list))
    for i in _list:
        print(*i)
    return None

hanoi(int(input()))