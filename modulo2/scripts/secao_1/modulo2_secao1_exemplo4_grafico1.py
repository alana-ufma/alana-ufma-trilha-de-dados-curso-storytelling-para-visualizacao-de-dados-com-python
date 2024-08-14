import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# Dados de exemplo
datas = pd.date_range(start='2023-01-01', periods=10, freq='D')
valores = [10, 12, 15, 14, 13, 16, 18, 17, 19, 20]

# Criação do DataFrame
df = pd.DataFrame({'Data': datas, 'Valor': valores})

# Gráfico de linhas
plt.plot(df['Data'], df['Valor'], marker='o')
plt.xlabel('Data')
plt.ylabel('Valor')
plt.title('Gráfico de Linhas de Séries Temporais')

# Formatação personalizada dos rótulos de data
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))

# Rotacionar os rótulos de data
plt.xticks(rotation=45)  # Rotaciona os rótulos em 45 graus

plt.tight_layout()  # Ajusta layout para evitar cortes
plt.show()
