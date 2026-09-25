a, s = input().split()
a = int(a)
group_len = len(s) // a
res = ''
for i in range(0, len(s), group_len):
    res += s[i:i+group_len][::-1]
print(res)


        


