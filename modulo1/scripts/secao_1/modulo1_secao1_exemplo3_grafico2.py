# Gráfico de Linhas do Percentual de Promoções por Gênero:
import matplotlib.pyplot as plt
import os
# Dados
anos = [2016, 2017, 2018, 2019, 2020]
promocoes_homens = [15, 18, 20, 22, 25]
promocoes_mulheres = [10, 12, 14, 16, 18]

# Configuração do gráfico
plt.plot(anos, promocoes_homens, marker='o', linestyle='-', color='b', label='Homens')
plt.plot(anos, promocoes_mulheres, marker='o', linestyle='-', color='r', label='Mulheres')

# Labels e título
plt.xlabel('Ano')
plt.ylabel('Percentual de Promoções (%)')
plt.title('Percentual de Promoções por Gênero (2016-2020)')
plt.legend()
plt.show()