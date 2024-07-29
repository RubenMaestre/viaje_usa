# paginas/ruta.py
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

def display():
    # Título de la página
    st.markdown("<h1 style='text-align: center;'>Ruta</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Cargar el DataFrame con los metadatos
    df = pd.read_csv('data/metadata.csv')

    # Crear un mapa centrado en los EE. UU.
    map_center = [39.8283, -98.5795]
    map = folium.Map(location=map_center, zoom_start=4)

    # Añadir marcadores al mapa
    for idx, row in df.iterrows():
        if pd.notnull(row['latitude']) and pd.notnull(row['longitude']):
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=f"<b>{row['file_name']}</b><br>{row['date_time']}",
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(map)

    # Mostrar el mapa en Streamlit
    folium_static(map)
