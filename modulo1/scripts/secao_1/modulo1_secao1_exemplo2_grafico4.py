import matplotlib.pyplot as plt
import os
"""
# Gráfico de Linhas das Espécies Vulneráveis
"""
# Dados
anos = [2000, 2005, 2010, 2015, 2020]
populacao_especie_a = [100, 80, 70, 60, 40]
populacao_especie_b = [100, 85, 75, 70, 50]
populacao_especie_c = [100, 70, 60, 50, 30]

# Configuração do gráfico
plt.plot(anos, populacao_especie_a, marker='o', linestyle='-', color='r', label='Espécie A')
plt.plot(anos, populacao_especie_b, marker='o', linestyle='-', color='b', label='Espécie B')
plt.plot(anos, populacao_especie_c, marker='o', linestyle='-', color='g', label='Espécie C')

# Labels e título
plt.xlabel('Ano')
plt.ylabel('População Relativa (%)')
plt.title('Declínio das Populações de Espécies Vulneráveis (2000-2020)')
plt.legend()
plt.show()