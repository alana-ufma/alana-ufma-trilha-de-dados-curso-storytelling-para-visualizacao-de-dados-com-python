import matplotlib.pyplot as plt
import os
"""
# Gráfico de Linhas da Temperatura Média Anual
"""
# Dados
anos = [2000, 2005, 2010, 2015, 2020]
temperaturas = [22.5, 23.0, 23.5, 24.0, 24.5]

# Configuração do gráfico
plt.plot(anos, temperaturas, marker='o', linestyle='-', color='r')

# Labels e título
plt.xlabel('Ano')
plt.ylabel('Temperatura Média Anual (°C)')
plt.title('Aumento da Temperatura Média Anual (2000-2020)')
plt.show()