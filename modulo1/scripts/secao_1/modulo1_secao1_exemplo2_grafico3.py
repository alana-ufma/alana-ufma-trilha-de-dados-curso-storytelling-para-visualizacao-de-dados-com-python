import matplotlib.pyplot as plt
import os
"""
# Gráfico de Barras do Número de Espécies
"""
# Dados
anos = [2000, 2005, 2010, 2015, 2020]
especies = [150, 145, 140, 130, 120]

# Configuração do gráfico
plt.bar(anos, especies, color='g')

# Labels e título
plt.xlabel('Ano')
plt.ylabel('Número de Espécies')
plt.title('Declínio no Número de Espécies (2000-2020)')
plt.show()