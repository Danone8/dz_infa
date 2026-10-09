import numpy as np
import matplotlib.pyplot as plt

avg = 0
b = 10
sizes = [100, 1000, 10000, 100000]

plt.figure(figsize=(12, 8))

for i in range(4):
    size = sizes[i]
    values = np.random.normal(avg, b, size)

    plt.subplot(2, 2, i + 1)
    plt.hist(values, bins=100, range=(-50, 50), density=True)
    plt.title(f'Количество точек: {size}')
    plt.xlabel('Значение')
    plt.ylabel('Плотность')

plt.tight_layout()
plt.show()