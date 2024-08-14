# Gráfico de Linhas do Percentual de Funcionários em Posições de Liderança por Gênero:
import matplotlib.pyplot as plt
import os
# Dados
anos = [2016, 2017, 2018, 2019, 2020]
lideranca_homens = [80, 78, 75, 73, 70]
lideranca_mulheres = [20, 22, 25, 27, 30]

# Configuração do gráfico
plt.plot(anos, lideranca_homens, marker='o', linestyle='-', color='b', label='Homens')
plt.plot(anos, lideranca_mulheres, marker='o', linestyle='-', color='r', label='Mulheres')

# Labels e título
plt.xlabel('Ano')
plt.ylabel('Percentual em Posições de Liderança (%)')
plt.title('Percentual de Funcionários em \nPosições de Liderança por Gênero (2016-2020)')
plt.legend()
plt.show()
