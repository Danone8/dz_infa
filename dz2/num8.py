n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    c_more = 0
    c_less = 0
    for j in range(n):
        if a[i] > a[j]:
            c_more += 1
        elif a[i] < a[j]:
            c_less += 1
    if c_more == c_less:
        print(a[i])
        break