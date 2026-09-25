with open('text.txt', 'r') as f:
    a = f.read()
count = 0
flag = False
for el in a:
    if el in '.?!':
        if not flag:
            count += 1
            flag = True
    else:
        flag = False
print(count)
