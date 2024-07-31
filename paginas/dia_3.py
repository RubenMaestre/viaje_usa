# paginas/dia_3.py
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

def display():
    # Título de la página
    st.markdown("<h1 style='text-align: center;'>Día 3</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Introducción del día
    st.markdown("""
        <div style='text-align: justify; font-size: 18px;'>
            Este es el mapa de la ruta correspondiente al Día 3 de nuestro viaje. 
            Las siguientes paradas reflejan los momentos y lugares que visitamos el tercer día.
        </div>
        <br><br>
    """, unsafe_allow_html=True)

    # Cargar el DataFrame con los metadatos desde el archivo CSV
    df = pd.read_csv('data/df_unido.csv')

    # Filtrar filas con el día 3 (correspondiente al número 4 en la columna 'dia')
    df_dia_3 = df[df['dia'] == 4].sort_values(by='date_time').reset_index(drop=True)

    # Crear un mapa centrado en Manhattan
    map_center = [40.7831, -73.9712]
    map = folium.Map(location=map_center, zoom_start=12)

    # Añadir marcadores al mapa
    coordinates = []
    for idx, row in df_dia_3.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"<b>{row['file_name']}</b><br>{row['date_time']}",
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(map)
        coordinates.append((row['latitude'], row['longitude']))

    # Definir segmentos de la ruta con colores y modos de transporte
    segmentos = [
        {'start': 'IMG_5808.JPG', 'end': 'IMG_5821.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_5821.JPG', 'end': 'IMG_5836.JPG', 'color': 'green', 'mode': 'TREN'},
        {'start': 'IMG_5836.JPG', 'end': 'IMA_STATION.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMA_STATION.JPG', 'end': 'IMA_PENST.JPG', 'color': 'green', 'mode': 'TREN'},
        {'start': 'IMA_PENST.JPG', 'end': 'IMA_HTROOSL.JPG', 'color': 'red', 'mode': 'ANDANDO'}
    ]

    # Función para obtener el índice de una imagen
    def get_index(df, file_name):
        indices = df.index[df['file_name'] == file_name].tolist()
        if indices:
            return indices[0]
        else:
            return None

    # Añadir líneas de ruta al mapa
    for segment in segmentos:
        start_idx = get_index(df_dia_3, segment['start'])
        end_idx = get_index(df_dia_3, segment['end'])
        if start_idx is not None and end_idx is not None:
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
            <span style='color: red;'>■</span> Andando<br>
            <span style='color: green;'>■</span> Tren<br>
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
