a,b,c=map(int,input().split())
if 1<=a<=20 and 1<=b<=100 and 2<=c<=100:
    s=(a ** b)%c
    print(s)