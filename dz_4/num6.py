import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data = pd.read_csv('BTC_data.csv')
data['time'] = pd.to_datetime(data['time'])
data = data.sort_values('time')
dates = data['time']
x = (dates - dates.min()).dt.total_seconds().to_numpy() / 86400
y = data['close'].to_numpy()
z = np.polyfit(x, y, 3)
p = np.poly1d(z)


fig = plt.figure(figsize=(16, 9))
ax = fig.add_subplot(111)
ax.plot(dates, y, label='Цена биткоина')
ax.plot(dates, p(x), color='red', label='Полином третьей степени')
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y', tz=dates.dt.tz))

ax.set_xlabel('Дата')
ax.set_ylabel('Цена закрытия')
ax.set_title('Аппроксимация цены биткоина')
ax.legend()
ax.grid()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()