with open('input.txt', 'r') as f1:
    lines = f1.readlines()
    sys = int(lines[2][0])
    op = lines[1].strip()
    numbers = lines[0].split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i], sys)
    if op == '+':
        res = sum(numbers)
    elif op == '-':
        res = numbers[0]
        for i in numbers[1:]:
            res -= 1
    else:
        res = 1
        for i in numbers:
            res = res*i
fnres = ''           
while res:
    fnres = str(res%sys) + fnres
    res //= sys
with open('output.txt', 'w') as f2:
    f2.write(str(fnres))