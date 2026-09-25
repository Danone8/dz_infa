n, b, c = input().split()
p = int(n, int(b))
res = ''
while p:
    res = str(p%int(c)) + res
    p //= int(c)
if n == '0': print(0)
else: print(res)
