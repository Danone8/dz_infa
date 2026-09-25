a = input().split()
ans = 0
mx = 0
for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    if count > mx:
        mx = count
        ans = a[i]
print(ans)