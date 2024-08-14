import matplotlib.pyplot as plt

# Dados
altura = [170, 160, 180, 175, 165]
peso = [70, 60, 80, 75, 65]

# Configuração do gráfico
plt.scatter(altura, peso, color='green')

# Labels e título
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação entre Altura e Peso')

plt.show()