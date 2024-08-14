import matplotlib.pyplot as plt

# Dados
tipos_produto = ['Eletrônicos', 'Roupas', 'Alimentos', 'Móveis']
quantidade_vendida = [150, 200, 300, 100]

# Configuração do gráfico
plt.bar(tipos_produto, quantidade_vendida, color=['blue', 'green', 'red', 'purple'])

# Labels e título
plt.xlabel('Tipo de Produto')
plt.ylabel('Quantidade Vendida')
plt.title('Quantidade de Produtos Vendidos por Tipo')

plt.show()