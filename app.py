import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv(r'C:\Users\juan.ossa\Documents\Ts\tripelten\vehicles_us.csv')
st.title("Análisis de Vehículos Usados")

st.header("Visualizaciones disponibles")
hist_button = st.button('Construir histograma')
dispersion_button = st.button('Construir gráfico de dispersión')
condition_button = st.checkbox('Construir gráfico de categorías por condición del carro')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if dispersion_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

if condition_button:
    st.write('Creación de un gráfico de categorías por condición del carro')
    fig = px.bar(car_data, x="condition")
    fig.update_xaxes(type='category')
    st.plotly_chart(fig, use_container_width=True)
