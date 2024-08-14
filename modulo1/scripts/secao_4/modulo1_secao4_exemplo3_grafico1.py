import matplotlib.pyplot as plt
import seaborn as sns

# Dados
idades = [22, 25, 29, 30, 35, 40, 45, 50, 55, 60]

# Configuração do histograma
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist(idades, bins=5, edgecolor='black')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.title('Distribuição de Idades (Histograma)')

# Configuração do gráfico de densidade
plt.subplot(1, 2, 2)
sns.kdeplot(idades, shade=True, color='blue')
plt.xlabel('Idade')
plt.ylabel('Densidade')
plt.title('Distribuição de Idades (Gráfico de Densidade)')

plt.tight_layout()
plt.show()