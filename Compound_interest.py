p,r,t=map(int,input().split())
CI=p*((1+r/100) ** t)
print("%.2f" %CI)