n = int(input())
sp = [int(input()) for el in range(n-1)]
res = 0
for i in range(1, n+1):
    res = res ^ i
for el in sp:
    res = res ^el
print(res)

