# Gráfico de Barras do Salário Médio Anual por Gênero e Posição:
import matplotlib.pyplot as plt
import os
import numpy as np
# Dados
posicoes = ['Desenv. Júnior', 'Desenv. Sênior', 'Ger. de Projetos', 'Diretor de TI']
salarios_homens = [70000, 100000, 120000, 150000]
salarios_mulheres = [65000, 90000, 110000, 130000]

# Configuração do gráfico
x = np.arange(len(posicoes))
width = 0.25

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, salarios_homens, width, label='Homens')
rects2 = ax.bar(x + width/2, salarios_mulheres, width, label='Mulheres')

# Labels e título
ax.set_xlabel('Posição')
ax.set_ylabel('Salário Médio Anual (USD)')
ax.set_title('Salário Médio Anual por Gênero e Posição')
ax.set_xticks(x)
ax.set_xticklabels(posicoes) 
ax.legend()
plt.tight_layout()  
plt.show()