n=int(input())
se=0
a=list(map(int,input().split()))
for i in range(len(a)):
    se+=a[i]
print(se)