import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import pandas as pd
from mplfinance.original_flavor import candlestick_ohlc

# Dados de exemplo
datas = pd.date_range(start='2023-01-01', periods=10, freq='D')

ohlc = [
    [mdates.date2num(datas[i]), 10+i, 12+i, 9+i, 11+i] for i in range(len(datas))
]

# Configuração do gráfico de velas
fig, ax = plt.subplots()
candlestick_ohlc(ax, ohlc, width=0.6, colorup='g', colordown='r')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mticker.MaxNLocator(10))
plt.xlabel('Data')
plt.ylabel('Preço')
plt.title('Gráfico de Velas de Séries Temporais')

# Formatação personalizada dos rótulos de data
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))

# Rotacionar os rótulos de data
plt.xticks(rotation=45)  # Rotaciona os rótulos em 45 graus
plt.tight_layout()  # Ajusta layout para evitar cortes

plt.show()