import os
import folium
import json
import pandas as pd

# Coordenadas centrais do Maranhão
latitude_centro = -4.9609
longitude_centro = -44.6737

# Criação do mapa centrado no Maranhão
mapa = folium.Map(location=[latitude_centro, longitude_centro], zoom_start=7)

# Dados de exemplo: taxa de analfabetismo e taxa de desemprego em alguns municípios do Maranhão
dados_municipios = {
    "Municipio": ["São Luís", "Imperatriz", "Caxias", "Timon", "São José de Ribamar", "Açailândia", "Bacabal", "Balsas", "Codó", "Santa Inês"],
    "Taxa_Analfabetismo": [4.5, 6.2, 8.8, 7.5, 5.7, 10.4, 12.1, 9.3, 13.6, 11.9],
    "Taxa_Desemprego": [8.0, 9.5, 10.2, 9.8, 8.7, 12.3, 13.1, 11.0, 14.5, 13.0]
}

# Converter os dados para um DataFrame do Pandas
df = pd.DataFrame(dados_municipios)

# Obter o diretório onde o script está sendo executado
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Caminho para o arquivo GeoJSON na subpasta 'geojson'
caminho_geojson = os.path.join(diretorio_atual, 'geojson', 'maranhao_municipios.json')

# Carregar o arquivo GeoJSON com os limites dos municípios do Maranhão
with open(caminho_geojson, 'r') as f:
    geojson_data = json.load(f)

# Adicionar o mapa coroplético para a taxa de analfabetismo
folium.Choropleth(
    geo_data=geojson_data,
    name='choropleth',
    data=df,
    columns=['Municipio', 'Taxa_Analfabetismo'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Taxa de Analfabetismo (%)'
).add_to(mapa)

# Adicionar o mapa coroplético para a taxa de desemprego
folium.Choropleth(
    geo_data=geojson_data,
    name='choropleth',
    data=df,
    columns=['Municipio', 'Taxa_Desemprego'],
    key_on='feature.properties.name',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Taxa de Desemprego (%)'
).add_to(mapa)

# Adicionar controle de camadas
folium.LayerControl().add_to(mapa)

# Salvar o mapa como um arquivo HTML
mapa.save("combined_choropleth_map_maranhao.html")