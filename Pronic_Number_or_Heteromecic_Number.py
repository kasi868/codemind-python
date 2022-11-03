def isPronic(n):
  c = 0
  a = n + 1
  for i in range(0,a):
    if i * (i + 1) == n:
      c = 1
      break
  if c== 1:
    print("YES")
  else:
    print("NO")
n=int(input())
isPronic(n)