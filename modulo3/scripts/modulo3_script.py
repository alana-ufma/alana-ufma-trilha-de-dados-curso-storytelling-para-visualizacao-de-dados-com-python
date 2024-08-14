import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
st.set_page_config(layout="wide")

# Dados fictícios
dados = {
    'Municipio': ['São Luís', 'São José de Ribamar', 'Paço do Lumiar', 'Raposa'],
    '2016': [1200, 500, 300, 150],
    '2017': [1300, 550, 350, 200],
    '2018': [1400, 600, 400, 250],
    '2019': [1500, 650, 450, 300],
    '2020': [1600, 700, 500, 350]
}

df = pd.DataFrame(dados)
df = df.set_index('Municipio')


col1, col2, col3  = st.columns(3)

with col1:
    st.subheader('Análise Exploratória dos Dados')
    st.write(df.describe())

with col2:

    st.subheader('Identificação de Tendências')
    fig, ax = plt.subplots()
    for municipio in df.index:
        ax.plot(df.columns, df.loc[municipio], marker='o', label=municipio)
    ax.set_title('Tendência de Doenças Respiratórias por Município')
    ax.set_xlabel('Ano')
    ax.set_ylabel('Número de Casos')
    ax.legend()
    st.pyplot(fig)

with col3:
        
    # Mapa de Calor
    st.subheader('Mapa de Calor da Incidência de Doenças Respiratórias')
    fig, ax = plt.subplots()
    sns.heatmap(df, annot=True, cmap='YlOrRd', fmt='d', ax=ax)
    ax.set_title('Incidência de Doenças Respiratórias (2016-2020)')
    ax.set_xlabel('Ano')
    ax.set_ylabel('Município')
    st.pyplot(fig)