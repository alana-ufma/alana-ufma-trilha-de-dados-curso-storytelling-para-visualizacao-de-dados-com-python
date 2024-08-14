import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
datas = pd.date_range(start='2023-01-01', periods=10, freq='D')
valores = [10, 12, 15, 14, 13, 16, 18, 17, 19, 20]

# Criação do DataFrame
df = pd.DataFrame({'Data': datas, 'Valor': valores})

# Cálculo da média móvel
df['Média Móvel'] = df['Valor'].rolling(window=3).mean()

# Gráfico
plt.plot(df['Data'], df['Valor'], marker='o', label='Original')
plt.plot(df['Data'], df['Média Móvel'], marker='o', label='Média Móvel')
plt.xlabel('Data')
plt.ylabel('Valor')
plt.title('Média Móvel')
plt.legend()
plt.xticks(rotation=45)  # Rotaciona os rótulos em 45 graus
plt.tight_layout()  # Ajusta layout para evitar cortes
plt.show()