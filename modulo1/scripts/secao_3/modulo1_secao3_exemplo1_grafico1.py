import matplotlib.pyplot as plt

# Dados
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Móveis']
quantidade_vendida = [150, 200, 300, 100]

# Configuração do gráfico
plt.bar(categorias, quantidade_vendida, color=['blue', 'green', 'red', 'purple'])

# Labels e título
plt.xlabel('Categoria')
plt.ylabel('Quantidade Vendida')
plt.title('Quantidade de Produtos Vendidos por Categoria')

plt.show()