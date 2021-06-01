import sys
a=list(map(int,sys.stdin.readline().split()))
det=a[0]
mode=0
for i in range(1,len(a)):
    if a[i]>det:
        if mode==0 or mode==1:
            mode=1
        else:
            mode=3
            break
    elif a[i]<det:
        if mode==0 or mode ==2:
            mode=2
        else:
            mode=3
            break
    det=a[i]
if mode==1:
    print('ascending')
elif mode==2:
    print('descending')
else:
    print('mixed')