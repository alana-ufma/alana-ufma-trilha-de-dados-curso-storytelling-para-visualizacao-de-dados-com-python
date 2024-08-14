import seaborn as sns
import matplotlib.pyplot as plt

# Dados
idades = [22, 25, 29, 30, 35, 40, 45, 50, 55, 60]

# Configuração do gráfico de densidade
sns.kdeplot(idades, shade=True, color='blue')

# Labels e título
plt.xlabel('Idade')
plt.ylabel('Densidade')
plt.title('Distribuição de Idades (Gráfico de Densidade)')

plt.show()