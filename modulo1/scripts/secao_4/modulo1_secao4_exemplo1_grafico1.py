import matplotlib.pyplot as plt

# Dados
idades = [22, 25, 29, 30, 35, 40, 45, 50, 55, 60]

# Configuração do histograma
plt.hist(idades, bins=5, edgecolor='black')

# Labels e título
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.title('Distribuição de Idades')

plt.show()