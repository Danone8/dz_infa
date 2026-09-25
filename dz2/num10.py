with open('text.txt', 'r', encoding='utf-8') as f:
    a = f.read()
glasn = 'уеыаоэяиюё'
res = ''
for i in range(len(a)):
    res += a[i]
    if i == 0:
        if a[0] in glasn:
            if a[1] not in glasn:
                res += 'с' + a[0]
            else:
                continue
    elif a[i] in glasn and a[i-1] == ' ' and a[i+1] in glasn: continue
    else:
        if a[i] in glasn and a[i-1] not in glasn:
            res += 'с' + a[i]

print(res)

            