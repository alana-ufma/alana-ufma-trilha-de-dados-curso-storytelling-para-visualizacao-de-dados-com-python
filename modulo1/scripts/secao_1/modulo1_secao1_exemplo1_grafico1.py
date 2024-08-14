import matplotlib.pyplot as plt
import os
"""
Gráfico de Barras das Vendas Trimestrais por Linha de Produto 
"""
# Dados
produtos = ['Eletrônicos', 'Vestuário', 'Utensílios Domésticos']
vendas_q1 = [500, 300, 200]
vendas_q2 = [450, 280, 150]
vendas_q3 = [400, 260, 100]

# Configuração do gráfico
fig, ax = plt.subplots()
bar_width = 0.2
index = range(len(produtos))

# Barras
bar1 = plt.bar(index, vendas_q1, bar_width, label='T1')
bar2 = plt.bar([i + bar_width for i in index], vendas_q2, bar_width, label='T2')
bar3 = plt.bar([i + 2 * bar_width for i in index], vendas_q3, bar_width, label='T3')

# Labels e título
plt.xlabel('Produtos')
plt.ylabel('Vendas (em milhares)')
plt.title('Vendas Trimestrais por Linha de Produto')
plt.xticks([i + bar_width for i in index], produtos)
plt.legend()
plt.show()

