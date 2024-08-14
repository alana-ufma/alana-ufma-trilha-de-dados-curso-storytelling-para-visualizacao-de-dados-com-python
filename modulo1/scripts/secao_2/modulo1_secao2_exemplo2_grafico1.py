import matplotlib.pyplot as plt

# Dados
nivel_satisfacao = ['Muito \nInsatisfeito', 'Insatisfeito', 'Neutro', 'Satisfeito', 'Muito Satisfeito']
numero_respostas = [10, 20, 30, 25, 15]

# Configuração do gráfico
plt.bar(nivel_satisfacao, numero_respostas, color='orange')

# Labels e título
plt.xlabel('Nível de Satisfação')
plt.ylabel('Número de Respostas')
plt.title('Nível de Satisfação dos Clientes')
plt.tight_layout()

plt.show()