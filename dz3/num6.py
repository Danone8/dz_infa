import numpy as np
def mnk(x, y):
    x = np.array(x)
    y = np.array(y)
    k = (np.mean(x * y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)
    b = np.mean(y) - k * np.mean(x)
    return k, b
x, y = list(map(float, input().split())), list(map(float, input().split()))
k, b = mnk(x, y)
print(k, b)