import matplotlib.pyplot as plt
import os
"""
# Gráfico de Linhas do Feedback de Clientes
"""
# Dados
meses = ['Julho', 'Agosto', 'Setembro']
reclamacoes = [50, 65, 85]

# Configuração do gráfico
plt.plot(meses, reclamacoes, marker='o', linestyle='-', color='r')

# Labels e título
plt.xlabel('Meses')
plt.ylabel('Número de Reclamações')
plt.title('Reclamações sobre Utensílios Domésticos')
plt.show()