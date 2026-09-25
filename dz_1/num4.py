with open('input.txt', 'r') as f1:
    lines = f1.readlines()
    op = lines[1].strip()
    numbers = list(map(int, lines[0].split()))
    if op == '+':
        res = sum(numbers)
    elif op == '-':
        res = numbers[0]
        for i in numbers[1:]:
            res -= i
    else:
        res = 1
        for i in numbers:
            res = res*i
with open('output.txt', 'w') as f2:
    f2.write(str(res))