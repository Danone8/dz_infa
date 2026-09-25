k = int(input())
st = input()
res = ''
for i in range(0, len(st), k):
    res += st[i:i+3][::-1]
print(res)
