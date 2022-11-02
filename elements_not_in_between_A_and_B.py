n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in l:
    if (a>i or i>b):
        print(i,end=' ')
        s+=i
if s==0:
    print(-1)