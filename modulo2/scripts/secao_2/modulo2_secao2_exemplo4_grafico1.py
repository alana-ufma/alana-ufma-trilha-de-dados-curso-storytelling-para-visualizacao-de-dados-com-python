import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Dados de exemplo
datas = pd.date_range(start='2023-01-01', periods=10, freq='D')
valores = [10, 12, 15, 14, 13, 16, 18, 17, 19, 20]

# Criação do DataFrame
df = pd.DataFrame({'Data': datas, 'Valor': valores})

# Ajuste do modelo de suavização exponencial
modelo = ExponentialSmoothing(df['Valor'], trend='add', seasonal=None, seasonal_periods=None)
ajuste = modelo.fit()

# Previsão
df['Suavização Exponencial'] = ajuste.fittedvalues

# Gráfico
plt.plot(df['Data'], df['Valor'], marker='o', label='Original')
plt.plot(df['Data'], df['Suavização Exponencial'], marker='o', label='Suavização Exponencial')
plt.xlabel('Data')
plt.ylabel('Valor')
plt.title('Suavização Exponencial')
plt.legend()
plt.xticks(rotation=45)  # Rotaciona os rótulos em 45 graus
plt.tight_layout()  # Ajusta layout para evitar cortes
plt.show()