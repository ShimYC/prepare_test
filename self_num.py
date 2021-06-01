from collections import deque
def d(n,L:list):
    ans=int(n)
    for i in n:
        ans+=int(i)
    if ans<=10000:
        if str(ans) in L:
            L.remove(str(ans))
            return d(str(ans),L)
        else:
            return None
    else:
        return None

numbers=deque([str(i) for i in range(1,10000+1)])
New_list=deque([])
while True:
    New_list.append(numbers[0])
    d(numbers[0],numbers)
    numbers.popleft()
    if len(numbers)==0:
        break
for i in New_list:
    print(i)