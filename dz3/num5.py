import numpy as np

n, m = map(int, input().split())
a = np.zeros((n, m), dtype=int)
i = j = 0
di, dj = 0, 1

for num in range(1, n * m + 1):
    a[i, j] = num
    ni = i + di
    nj = j + dj
    if not (0 <= ni < n and 0 <= nj < m) or a[ni, nj] != 0:
        di, dj = dj, -di
    i += di
    j += dj
print(a)
a = a * np.arange(n).reshape(n, 1)
print(a)