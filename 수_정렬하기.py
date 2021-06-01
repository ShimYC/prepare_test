import sys
n=input()
a=list(map(int,sys.stdin.readlines()))
a.sort()
for i in range(len(a)):
    print(a[i])