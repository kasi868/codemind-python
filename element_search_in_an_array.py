n=int(input())
a=list(map(int,input().split()))
b=int(input())
for i in range(len(a)):
    if a[i]==b:
        print("True")
        break
else:
    print("False")