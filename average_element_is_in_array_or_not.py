n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=i
b=s//n
if b in a:
    print("True")
else:
    print("False")