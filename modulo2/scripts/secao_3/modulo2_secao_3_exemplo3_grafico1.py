import os
import folium
import json

# Coordenadas centrais do Maranhão
latitude_centro = -4.9609
longitude_centro = -44.6737

# Criação do mapa centrado no Maranhão
mapa = folium.Map(location=[latitude_centro, longitude_centro], zoom_start=7)

# Dados de exemplo: taxa de analfabetismo em alguns municípios do Maranhão
taxa_analfabetismo = {
    "São Luís": 4.5,
    "Imperatriz": 6.2,
    "Caxias": 8.8,
    "Timon": 7.5,
    "São José de Ribamar": 5.7,
    "Açailândia": 10.4,
    "Bacabal": 12.1,
    "Balsas": 9.3,
    "Codó": 13.6,
    "Santa Inês": 11.9
}

# Obter o diretório onde o script está sendo executado
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Caminho para o arquivo GeoJSON na subpasta 'geojson'
caminho_geojson = os.path.join(diretorio_atual, 'geojson', 'maranhao_municipios.json')

# Carregar o arquivo GeoJSON com os limites dos municípios do Maranhão
with open(caminho_geojson, 'r') as f:
    geojson_data = json.load(f)

# Adicionar o mapa coroplético
folium.Choropleth(
    geo_data=geojson_data,
    name='choropleth',
    data=taxa_analfabetismo,
    columns=['Municipio', 'Taxa_Analfabetismo'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Taxa de Analfabetismo (%)'
).add_to(mapa)

# Adicionar controle de camadas
folium.LayerControl().add_to(mapa)

# Salvar o mapa como um arquivo HTML
mapa.save("choropleth_map_maranhao.html")