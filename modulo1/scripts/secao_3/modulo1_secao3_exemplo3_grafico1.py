import matplotlib.pyplot as plt
import seaborn as sns

# Dados para o gráfico de barras
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Móveis']
quantidade_vendida = [150, 200, 300, 100]

# Dados para o mapa de calor
dados = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Configuração do gráfico de barras
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(categorias, quantidade_vendida, color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Categoria')
plt.ylabel('Quantidade Vendida')
plt.title('Quantidade de Produtos Vendidos por Categoria')

# Configuração do mapa de calor
plt.subplot(1, 2, 2)
sns.heatmap(dados, annot=True, cmap='coolwarm')
plt.title('Mapa de Calor de Matriz')

plt.tight_layout()
plt.show()