a = input().split()
n = len(a)
pr = 1
for el in a:
    pr *= int(el)
print(pr**(1/n))
