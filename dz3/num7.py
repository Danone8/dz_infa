import numpy as np
def solve(a):
    a = np.array(a, dtype=float)
    A = a[:, :-1]
    b = a[:, -1]
    return np.linalg.solve(A, b)

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(float, input().split())))

x = solve(a)
print(*x)