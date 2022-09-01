a=int(input())
b=int(input())
s=0
t=0
for i in range(1,a+1):
    if a%i==0:
        s+=i
for j in range(1,b+1):
    if b%j==0:
        t+=j
if s==t:
    print("Amicable")
else:
    print("Not Amicable")