import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv(r'C:\Users\juan.ossa\Documents\Ts\tripelten\vehicles_us.csv') # leer los datos

hist_button = st.button('Construir histograma') # crear un botón
Dispersion_button = st.button('Construir Gráfico de Dispersión') # crear un botón
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

elif Dispersion_button:
    st.write('Creación de un Gráfico de Dispersión para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
     