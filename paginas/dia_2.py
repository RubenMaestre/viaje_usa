# paginas/dia_2.py
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import base64
import os

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

    # Añadir texto para interactuar con el mapa
    st.markdown("""
        <div style='text-align: justify; font-size: 18px;'>
            Amplía el mapa o desplázate por él para conocer nuestra ruta de este día. Los marcadores en rojo del mapa contienen fotografía e información sobre la imagen. 
            Los marcadores azules indican que estuvimos en ese lugar a la hora y fecha indicada.
        </div>
        <br><br>
    """, unsafe_allow_html=True)

    # Cargar el DataFrame con los metadatos desde el archivo CSV
    df = pd.read_csv('data/df_unido.csv')

    # Filtrar filas con el día 2 (correspondiente al número 3 en la columna 'dia')
    df_dia_2 = df[df['dia'] == 3].sort_values(by='date_time').reset_index(drop=True)

    # Crear un mapa centrado en Manhattan
    map_center = [40.71850, -74.00442]
    map = folium.Map(location=map_center, zoom_start=12)

    # Añadir marcadores al mapa
    coordinates = []
    for idx, row in df_dia_2.iterrows():
        if row['foto'] == 'SI':
            # Construir la ruta del archivo de imagen
            image_path = os.path.join('sources/fotos', row["enlace"])
            if os.path.exists(image_path):
                # Cargar la imagen
                encoded = base64.b64encode(open(image_path, 'rb').read()).decode()
                html = f"""
                <h4>{row['descripcion']}</h4>
                <img src="data:image/jpeg;base64,{encoded}" width="300" height="200">
                <br>{row['date_time']}
                """
                iframe = folium.IFrame(html, width=320, height=320)
                popup = folium.Popup(iframe, max_width=320)
                color = 'red'
            else:
                st.write(f"Archivo de imagen no encontrado: {image_path}")
                popup = folium.Popup(f"<b>{row['file_name']}</b><br>{row['date_time']}", max_width=250)
                color = 'blue'
        else:
            popup = folium.Popup(f"<b>{row['file_name']}</b><br>{row['date_time']}", max_width=250)
            color = 'blue'
        
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=popup,
            icon=folium.Icon(color=color, icon='info-sign')
        ).add_to(map)
        coordinates.append((row['latitude'], row['longitude']))

    # Definir segmentos de la ruta con colores y modos de transporte
    segmentos = [
        {'start': 'HOTEL.JPG', 'end': 'IMG_5486.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_5486.JPG', 'end': 'IMG_5492.JPG', 'color': 'yellow', 'mode': 'METRO'},
        {'start': 'IMG_5492.JPG', 'end': 'IMG_5519.JPG', 'color': 'blue', 'mode': 'FERRY'},
        {'start': 'IMG_5519.JPG', 'end': 'IMG_3623.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_3623.JPG', 'end': 'IMG_5610.JPG', 'color': 'blue', 'mode': 'FERRY'},
        {'start': 'IMG_5610.JPG', 'end': 'IMG_3674.JPG', 'color': 'red', 'mode': 'ANDANDO'}
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
        start_idx = get_index(df_dia_2, segment['start'])
        end_idx = get_index(df_dia_2, segment['end'])
        if start_idx is not None and end_idx is not None:
            segment_coords = coordinates[start_idx:end_idx + 1]
            if segment_coords:
                folium.PolyLine(segment_coords, color=segment['color'], weight=2.5, opacity=1).add_to(map)
            else:
                st.write(f"Segmento vacío: {segment['start']} a {segment['end']}")
        else:
            st.write(f"Segmento no encontrado: {segment['start']} a {segment['end']}")

    # Configurar columnas para centrar el mapa
    col1, col2 = st.columns([1, 9])  # Ajustar el ancho de las columnas

    with col2:
        folium_static(map, width=1080, height=720)  # Ajusta el tamaño del mapa

    # Añadir leyenda en la columna izquierda
    with col1:
        st.markdown("""
            <div style='text-align: left; font-size: 18px;'>
                <b>Leyenda</b><br>
                <span style='color: yellow;'>■</span> Metro<br>
                <span style='color: blue;'>■</span> Ferry<br>
                <span style='color: red;'>■</span> Andando<br>
                <br>
                <b>Marcadores</b><br>
                <span style='color: red;'>■</span> Con Foto<br>
                <span style='color: blue;'>■</span> Sin Foto<br>
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
