import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('iris_data.csv')
species = data['Species'].value_counts()
length = data['PetalLengthCm']
counts = [(length <= 1.2).sum(), ((length > 1.2) & (length < 1.5)).sum(), (length >= 1.5).sum()]

fig = plt.figure(figsize=(16, 9))

ax1 = fig.add_subplot(121)
ax1.pie(species.values, labels=species.index, autopct='%1.1f%%')
ax1.set_title('Доли разных видов ирисов')

ax2 = fig.add_subplot(122)
ax2.pie(counts, labels=['≤ 1.2 см', '1.2 < длина < 1.5 см', '≥ 1.5 см'], autopct='%1.1f%%')
ax2.set_title('Доли ирисов по длине лепестка')

plt.tight_layout()
plt.show()