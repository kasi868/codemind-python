n=int(input())
se=0
so=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if a[i]%2==0:
        se+=a[i]
    else:
        so+=a[i]
print(so)