import folium

# Coordenadas de algumas cidades do Maranhão com hospitais
hospitais = [
    {"nome": "Hospital Universitário", "coordenadas": [-2.5297, -44.3028]},
    {"nome": "Hospital Municipal", "coordenadas": [-4.2325, -44.7844]},
    {"nome": "Hospital Geral", "coordenadas": [-3.7461, -42.5586]},
    {"nome": "Hospital Regional", "coordenadas": [-5.0892, -42.8019]},
    {"nome": "Hospital da Mulher", "coordenadas": [-2.5489, -44.0703]},
    {"nome": "Hospital Municipal", "coordenadas": [-4.1347, -44.1419]},
    {"nome": "Hospital Regional", "coordenadas": [-5.0978, -45.0916]},
    {"nome": "Hospital Municipal", "coordenadas": [-3.6821, -43.8979]},
    {"nome": "Hospital Geral", "coordenadas": [-4.2553, -43.9186]},
    {"nome": "Hospital Regional", "coordenadas": [-3.1190, -44.2475]}
]

# Criação do mapa centrado no Maranhão
mapa = folium.Map(location=[-4.9609, -44.6737], zoom_start=7)

# Adição dos pontos ao mapa
for hospital in hospitais:
    folium.Marker(
        location=hospital["coordenadas"],
        popup=hospital["nome"],
        icon=folium.Icon(color='red', icon='plus-sign')
    ).add_to(mapa)

# Exibição do mapa
mapa.save("point_map_hospitais_maranhao.html")