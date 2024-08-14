import seaborn as sns
import matplotlib.pyplot as plt

# Dados
dados = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Configuração do mapa de calor
sns.heatmap(dados, annot=True, cmap='coolwarm')

# Título
plt.title('Mapa de Calor de Matriz')

plt.show()