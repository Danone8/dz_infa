import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
data = pd.read_csv('BTC_data.csv')
dates = pd.to_datetime(data.iloc[:, 0])
close = data['close']
prices = pd.DataFrame({'date': dates, 'close': close}).sort_values('date')
fig = plt.figure(figsize=(16, 9))
ax = fig.add_subplot(111)

ax.plot(prices['date'], prices['close'])
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y'))

ax.set_xlabel('Дата')
ax.set_ylabel('Цена закрытия')
ax.set_title('Исторический график цены биткоина')
ax.grid()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()