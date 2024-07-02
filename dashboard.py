import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Título do dashboard
st.title('Dashboard de Dados 2022')

# Descrição do dashboard
st.markdown('Visualizações das competições de 2022')

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Carrega os dados
    data = pd.read_csv(uploaded_file)


    # Gráfico de posições por academia (Top 5)
    st.header('Posições por Academia (Top 5)')
    top_academies = data['Academy'].value_counts().nlargest(5).index
    filtered_data = data[data['Academy'].isin(top_academies)]
    fig_academy = px.histogram(filtered_data, y='Academy', title='Posições por Academia (Top 5)', histfunc='count')
    fig_academy.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_academy)


    # Gráfico de pizza com a quantidade por faixa (Belt)
    st.header('Distribuição de Faixas (Belt)')
    fig_belt_pie = px.pie(data, names='Belt', title='Distribuição de Faixas (Belt)')
    st.plotly_chart(fig_belt_pie)

else:
    st.warning('Por favor, faça o upload de um arquivo CSV para visualizar os dados.')
