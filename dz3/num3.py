def evk_ext(a, b):
    if b == 0:
        return a, 1, 0
    d, x1, y1 = evk_ext(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return d, x, y

def find_answ(a, b):
    d, x0, y0 = evk_ext(a, b)
    a1 = a // d
    b1 = b//d
    kx = (-x0)// b1
    ky = y0 // a1
    variants = [kx, kx + 1, ky, ky + 1]
    best_x = None
    best_y = None

    for k in variants:
        x = x0 + k * b1
        y = y0 - k * a1
        if best_x is None:
            best_x = x
            best_y = y
        elif abs(x) + abs(y) < abs(best_x) + abs(best_y):
            best_x = x
            best_y = y
        elif abs(x) + abs(y) == abs(best_x) + abs(best_y) and x < best_x:
            best_x = x
            best_y = y
    return best_x, best_y, d

a, b = list(map(int, input().split()))
x, y, d = find_answ(a, b)
print(x, y, d)
