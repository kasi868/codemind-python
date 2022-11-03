n,m=map(int,input().split())
if n>m:
    s=n
else:
    s=m
while True:
    if s%n==0 and s%m==0:
        print(s)
        break
    s+=1