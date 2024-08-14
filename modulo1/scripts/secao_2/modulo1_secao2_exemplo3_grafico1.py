import matplotlib.pyplot as plt

# Dados
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
temperaturas = [25, 26, 28, 30, 32, 33, 35, 34, 32, 30, 28, 26]

# Configuração do gráfico
plt.plot(meses, temperaturas, marker='o', linestyle='-', color='blue')

# Labels e título
plt.xlabel('Mês')
plt.ylabel('Temperatura Média (°C)')
plt.title('Temperatura Média Mensal')

plt.show()