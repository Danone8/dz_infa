import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('iris_data.csv')
columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
fig = plt.figure(figsize=(16, 12))
k = 1

for i in range(4):
    for j in range(i + 1, 4):
        x = data[columns[j]]
        y = data[columns[i]]
        a, b = np.polyfit(x, y, 1)
        x_line = np.linspace(x.min(), x.max(), 100)
        ax = fig.add_subplot(3, 2, k)
        ax.scatter(x, y, s=15)
        ax.plot(x_line, a * x_line + b, color='red', label=f'МНК: a = {a:.3f}, b = {b:.3f}')
        ax.set_xlabel(columns[j])
        ax.set_ylabel(columns[i])
        ax.legend()
        k += 1

plt.tight_layout()
plt.show()