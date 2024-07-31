# paginas/dia_4.py
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

def display():
    # Título de la página
    st.markdown("<h1 style='text-align: center;'>Día 4</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Introducción del día
    st.markdown("""
        <div style='text-align: justify; font-size: 18px;'>
            Este es el mapa de la ruta correspondiente al Día 4 de nuestro viaje. 
            Las siguientes paradas reflejan los momentos y lugares que visitamos el cuarto día.
        </div>
        <br><br>
    """, unsafe_allow_html=True)

    # Cargar el DataFrame con los metadatos desde el archivo CSV
    df = pd.read_csv('data/df_unido.csv')

    # Filtrar filas con el día 4 (correspondiente al número 5 en la columna 'dia')
    df_dia_4 = df[df['dia'] == 5].sort_values(by='date_time').reset_index(drop=True)

    # Crear un mapa centrado en Manhattan
    map_center = [39.72699, -75.58720]
    map = folium.Map(location=map_center, zoom_start=8)

    # Añadir marcadores al mapa
    coordinates = []
    for idx, row in df_dia_4.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"<b>{row['file_name']}</b><br>{row['date_time']}",
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(map)
        coordinates.append((row['latitude'], row['longitude']))

    # Definir segmentos de la ruta con colores y modos de transporte
    segmentos = [
        {'start': 'IMG_HOTROOSV.JPG', 'end': 'IMG_PENST.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_PENST.JPG', 'end': 'IMG_WAS_ST.JPG', 'color': 'green', 'mode': 'TREN'},
        {'start': 'IMG_WAS_ST.JPG', 'end': 'IMG_3746.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_3746.JPG', 'end': 'IMA_PENST2.JPG', 'color': 'green', 'mode': 'TREN'},
        {'start': 'IMA_PENST2.JPG', 'end': 'IMG_HTROOS.JPG', 'color': 'brown', 'mode': 'TAXI'}
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
        start_idx = get_index(df_dia_4, segment['start'])
        end_idx = get_index(df_dia_4, segment['end'])
        if start_idx is not None and end_idx is not None:
            segment_coords = coordinates[start_idx:end_idx + 1]
            if segment_coords:
                folium.PolyLine(segment_coords, color=segment['color'], weight=2.5, opacity=1).add_to(map)
            else:
                st.write(f"Segmento vacío: {segment['start']} a {segment['end']}")
        else:
            st.write(f"Segmento no encontrado: {segment['start']} a {segment['end']}")

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
            <span style='color: brown;'>■</span> Taxi<br>
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
