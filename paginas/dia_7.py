# paginas/dia_7.py
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

def display():
    # Título de la página
    st.markdown("<h1 style='text-align: center;'>Día 7</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Introducción del día
    st.markdown("""
        <div style='text-align: justify; font-size: 18px;'>
            Este es el mapa de la ruta correspondiente al Día 7 de nuestro viaje. 
            Las siguientes paradas reflejan los momentos y lugares que visitamos el séptimo día.
        </div>
        <br><br>
    """, unsafe_allow_html=True)

    # Cargar el DataFrame con los metadatos desde el archivo CSV
    df = pd.read_csv('data/df_unido.csv')

    # Filtrar filas con el día 7 (correspondiente al número 8 en la columna 'dia')
    df_dia_7 = df[df['dia'] == 8].sort_values(by='date_time').reset_index(drop=True)

    # Crear un mapa centrado en Manhattan
    map_center = [43.06100, -76.43506]
    map = folium.Map(location=map_center, zoom_start=9)

    # Añadir marcadores al mapa
    coordinates = []
    for idx, row in df_dia_7.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"<b>{row['file_name']}</b><br>{row['date_time']}",
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(map)
        coordinates.append((row['latitude'], row['longitude']))

    # Definir segmentos de la ruta con colores y modos de transporte
    segmentos = [
        {'start': 'IMG_3817.JPG', 'end': 'IMG_6360.JPG', 'color': 'blue', 'mode': 'COCHE'},
        {'start': 'IMG_6360.JPG', 'end': 'IMG_3885.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_3885.JPG', 'end': 'IMG_TOLEDO.JPG', 'color': 'blue', 'mode': 'COCHE'}
    ]

    # Función para obtener el índice de una imagen
    def get_index(df, file_name):
        indices = df.index[df['file_name'] == file_name].tolist()
        if indices:
            return indices[0]
        else:
            st.write(f"Archivo no encontrado: {file_name}")
            return None

    # Añadir líneas de ruta al mapa
    for segment in segmentos:
        start_idx = get_index(df_dia_7, segment['start'])
        end_idx = get_index(df_dia_7, segment['end'])
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
            <span style='color: blue;'>■</span> Coche<br>
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