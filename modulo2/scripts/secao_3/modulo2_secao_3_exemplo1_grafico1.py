import folium
from folium.plugins import HeatMap

# Coordenadas de algumas cidades do Maranhão com número de casos de COVID-19
dados = [
    [-2.5297, -44.3028, 800],  # São Luís
    [-4.2325, -44.7844, 600],  # Imperatriz
    [-3.7461, -42.5586, 700],  # Caxias
    [-5.0892, -42.8019, 500],  # Timon
    [-2.5489, -44.0703, 900],  # São José de Ribamar
    [-4.1347, -44.1419, 400],  # Açailândia
    [-5.0978, -45.0916, 600],  # Bacabal
    [-3.6821, -43.8979, 700],  # Balsas
    [-4.2553, -43.9186, 500],  # Codó
    [-3.1190, -44.2475, 800]   # Santa Inês
]

# Criação do mapa centrado no Maranhão
mapa = folium.Map(location=[-4.9609, -44.6737], zoom_start=7)

# Adição do Heatmap
HeatMap(dados).add_to(mapa)

# Exibição do mapa
mapa.save("heatmap_maranhao_covid.html")