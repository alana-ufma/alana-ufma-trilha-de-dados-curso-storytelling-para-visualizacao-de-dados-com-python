import matplotlib.pyplot as plt
import os
"""
# Gráfico de Linhas da Precipitação Anual
"""
# Dados
anos = [2000, 2005, 2010, 2015, 2020]
precipitacao = [1200, 1150, 1100, 1050, 1000]

# Configuração do gráfico
plt.plot(anos, precipitacao, marker='o', linestyle='-', color='b')

# Labels e título
plt.xlabel('Ano')
plt.ylabel('Precipitação Anual (mm)')
plt.title('Diminuição da Precipitação Anual (2000-2020)')
plt.show()