import numpy as np
import matplotlib.pyplot as plt
I = np.array([65.4, 97.8, 123.2, 160.2, 183.7, 217.7, 238.3, 267.3, 285.3, 306.7])
U = np.array([145, 215, 270, 350, 405, 480, 525, 590, 625, 675])
R = np.sum(I * U) / np.sum(I**2)

fig = plt.figure(figsize=(16, 9))
ax1 = fig.add_subplot(111)

ax1.scatter(I, U, marker='x', color='blue')

ax1.errorbar(I, U, yerr=3.8, color='k', linestyle='None', capsize=3)

ax1.plot(I, U, 'r', label=f'R = {R:.4f} Ом')

ax1.set_xlabel('I, мА')
ax1.set_ylabel('U, мВ')
ax1.set_title('Зависимость напряжения U от силы тока I (l = 20 см)')


ax1.grid()
ax1.legend()
plt.show()
