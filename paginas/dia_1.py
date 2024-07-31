# paginas/dia_1.py
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

def display():
    # Título de la página
    st.markdown("<h1 style='text-align: center;'>Día 1</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Introducción del día
    st.markdown("""
        <div style='text-align: justify; font-size: 18px;'>
            Este es el mapa de la ruta correspondiente al Día 1 de nuestro viaje. 
            Las siguientes paradas reflejan los momentos y lugares que visitamos el primer día.
        </div>
        <br><br>
    """, unsafe_allow_html=True)

    # Cargar el DataFrame con los metadatos desde el archivo Excel
    df = pd.read_excel('data/df_unido.xlsx')

    # Filtrar filas con el día 1 (correspondiente al número 2 en la columna 'dia')
    df_dia_1 = df[df['dia'] == 2]

    # Crear un mapa centrado en Manhattan
    map_center = [40.7831, -73.9712]
    map = folium.Map(location=map_center, zoom_start=12)

    # Añadir marcadores al mapa
    for idx, row in df_dia_1.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"<b>{row['file_name']}</b><br>{row['date_time']}",
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(map)

    # Configurar columnas para centrar el mapa
    col1, col2, col3 = st.columns([0.1, 7.8, 0.1])  # Ajustar el ancho de las columnas

    with col2:
        folium_static(map, width=1360, height=720)  # Ajusta el tamaño del mapa

    st.markdown("""
        <style>
            .stApp {
                max-width: 100%;
                padding: 0;
            }
        </style>
    """, unsafe_allow_html=True)

# Llamar a la función display para mostrar la página
display()
