def factorize(n):
    x = 2
    mn = []
    while x**2 <= n:
        while n%x == 0:
            mn.append(x)
            n //= x
        x += 1
    if n>1: mn.append(n)
    return mn
print(factorize(18))
