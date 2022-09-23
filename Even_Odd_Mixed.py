n=int(input())
s=n%10
n=n//10
a=n%10
n=n//10
if s%2==0 and a%2==0 and n%2==0:
    print("Even")
elif s%2==1 and a%2==1 and n%2==1:
    print("Odd")
else:
    print("Mixed")