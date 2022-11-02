n=int(input())
a=list(map(int,input().split()))
l=[]
for j in a:
    if j%2==1:
        l.append(j)
for i in a:
    if i%2==0:
        l.append(i)
for k in l:
    print(k,end=" ")