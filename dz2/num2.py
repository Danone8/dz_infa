k = int(input())
st = input()
res = ''
for i in range(0, len(st), k):
    res += st[i:i+k][::-1]
print(res)
