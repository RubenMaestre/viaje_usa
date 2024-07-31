# paginas/dia_2.py
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

def display():
    # Título de la página
    st.markdown("<h1 style='text-align: center;'>Día 2</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Introducción del día
    st.markdown("""
        <div style='text-align: justify; font-size: 18px;'>
            Este es el mapa de la ruta correspondiente al Día 2 de nuestro viaje. 
            Las siguientes paradas reflejan los momentos y lugares que visitamos el segundo día.
        </div>
        <br><br>
    """, unsafe_allow_html=True)

    # Cargar el DataFrame con los metadatos desde el archivo CSV
    df = pd.read_csv('data/df_unido.csv')

    # Filtrar filas con el día 2 (correspondiente al número 3 en la columna 'dia')
    df_dia_2 = df[df['dia'] == 3].sort_values(by='date_time').reset_index(drop=True)

    # Crear un mapa centrado en Manhattan
    map_center = [40.7831, -73.9712]
    map = folium.Map(location=map_center, zoom_start=12)

    # Añadir marcadores al mapa
    coordinates = []
    for idx, row in df_dia_2.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"<b>{row['file_name']}</b><br>{row['date_time']}",
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(map)
        coordinates.append((row['latitude'], row['longitude']))

    # Definir segmentos de la ruta con colores y modos de transporte
    segmentos = [
        {'start': 'IMG_5486.JPG', 'end': 'IMG_5492.JPG', 'color': 'yellow', 'mode': 'METRO'},
        {'start': 'IMG_5492.JPG', 'end': 'IMG_5519.JPG', 'color': 'blue', 'mode': 'FERRY'},
        {'start': 'IMG_5519.JPG', 'end': 'IMG_3623.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_3623.JPG', 'end': 'IMG_5610.JPG', 'color': 'blue', 'mode': 'FERRY'},
        {'start': 'IMG_5610.JPG', 'end': 'IMG_3674.JPG', 'color': 'red', 'mode': 'ANDANDO'}
    ]

    # Función para obtener el índice de una imagen
    def get_index(df, file_name):
        return df.index[df['file_name'] == file_name].tolist()[0]

    # Añadir líneas de ruta al mapa
    for segment in segmentos:
        start_idx = get_index(df_dia_2, segment['start'])
        end_idx = get_index(df_dia_2, segment['end'])
        segment_coords = coordinates[start_idx:end_idx + 1]
        folium.PolyLine(segment_coords, color=segment['color'], weight=2.5, opacity=1).add_to(map)

    # Configurar columnas para centrar el mapa
    col1, col2, col3 = st.columns([0.1, 7.8, 0.1])  # Ajustar el ancho de las columnas

    with col2:
        folium_static(map, width=1360, height=720)  # Ajusta el tamaño del mapa

    # Añadir leyenda debajo del mapa
    st.markdown("""
        <div style='text-align: center; font-size: 18px;'>
            <b>Leyenda</b><br>
            <span style='color: yellow;'>■</span> Metro<br>
            <span style='color: blue;'>■</span> Ferry<br>
            <span style='color: red;'>■</span> Andando<br>
        </div>
    """, unsafe_allow_html=True)

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
