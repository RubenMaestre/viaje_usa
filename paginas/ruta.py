# paginas/ruta.py
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import base64
import os

def display():
    # Título de la página
    st.markdown("<h1 style='text-align: center;'>Ruta</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Introducción del viaje
    st.markdown("""
        <div style='text-align: justify; font-size: 18px;'>
            Bienvenidos a la sección de la ruta de mi inolvidable viaje por Estados Unidos. 
            Entre el 28 de julio de 2013 y el 15 de agosto de 2013, recorrimos Estados Unidos 
            desde Nueva York hasta San Francisco en coche. Este viaje fue una experiencia única 
            y llena de aventuras que ahora puedo compartir gracias a la tecnología.
        </div>
        <br>
        <div style='text-align: justify; font-size: 18px;'>
            Gracias a las fotos almacenadas en mi iPhone, he podido extraer las coordenadas de 
            cada una y trazar la ruta exacta que seguimos. Cada marcador en el mapa representa 
            una parada, una vista espectacular o un momento especial capturado durante este 
            emocionante recorrido. Espero que disfruten este viaje virtual tanto como yo disfruté 
            haciéndolo.
        </div>
        <br><br>
    """, unsafe_allow_html=True)

    # Añadir texto para interactuar con el mapa
    st.markdown("""
        <div style='text-align: justify; font-size: 18px;'>
            Amplía el mapa o desplázate por él para conocer nuestra ruta de todo el viaje. Los marcadores en rojo del mapa contienen fotografía e información sobre la imagen. 
            Los marcadores azules indican que estuvimos en ese lugar a la hora y fecha indicada.
        </div>
        <br><br>
    """, unsafe_allow_html=True)

    # Cargar el DataFrame con los metadatos desde el archivo CSV
    df = pd.read_csv('data/df_unido.csv')

    # Filtrar filas con coordenadas no nulas
    df = df.dropna(subset=['latitude', 'longitude'])

    # Crear un mapa centrado en los EE. UU.
    map_center = [39.8283, -98.5795]
    map = folium.Map(location=map_center, zoom_start=4)

    # Añadir marcadores al mapa
    coordinates = []
    for idx, row in df.iterrows():
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

    # Definir todos los segmentos de la ruta con colores y modos de transporte
    segmentos = [
        # Día 1
        {'start': 'BARAJAS.JPG', 'end': 'LONDRES.JPG', 'color': 'pink', 'mode': 'AVIÓN'},
        {'start': 'LONDRES.JPG', 'end': 'IMG_3600.JPG', 'color': 'pink', 'mode': 'AVIÓN'},
        {'start': 'IMG_3600.JPG', 'end': 'HOTELROS.JPG', 'color': 'brown', 'mode': 'TAXI'},
        {'start': 'HOTELROS.JPG', 'end': 'IMG_5483.JPG', 'color': 'red', 'mode': 'ANDANDO'},


        # Día 2
        {'start': 'HOTEL.JPG', 'end': 'IMG_5486.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_5486.JPG', 'end': 'IMG_5492.JPG', 'color': 'yellow', 'mode': 'METRO'},
        {'start': 'IMG_5492.JPG', 'end': 'IMG_5519.JPG', 'color': 'blue', 'mode': 'FERRY'},
        {'start': 'IMG_5519.JPG', 'end': 'IMG_3623.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_3623.JPG', 'end': 'IMG_5610.JPG', 'color': 'blue', 'mode': 'FERRY'},
        {'start': 'IMG_5610.JPG', 'end': 'IMG_3674.JPG', 'color': 'red', 'mode': 'ANDANDO'},

        # Día 3
        {'start': 'IMG_5808.JPG', 'end': 'IMG_5821.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_5821.JPG', 'end': 'IMG_5836.JPG', 'color': 'green', 'mode': 'TREN'},
        {'start': 'IMG_5836.JPG', 'end': 'IMA_STATION.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMA_STATION.JPG', 'end': 'IMA_PENST.JPG', 'color': 'green', 'mode': 'TREN'},
        {'start': 'IMA_PENST.JPG', 'end': 'IMG_HTROOS.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_HTROOS.JPG', 'end': 'IMG_HTROOSL.JPG', 'color': 'red', 'mode': 'ANDANDO'},

        # Día 4
        {'start': 'IMG_HOTROOSV.JPG', 'end': 'IMG_PENST.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_PENST.JPG', 'end': 'IMG_WAS_ST.JPG', 'color': 'green', 'mode': 'TREN'},
        {'start': 'IMG_WAS_ST.JPG', 'end': 'IMG_3746.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_3746.JPG', 'end': 'IMA_PENST2.JPG', 'color': 'green', 'mode': 'TREN'},
        {'start': 'IMA_PENST2.JPG', 'end': 'IMG_HTROOS2.JPG', 'color': 'brown', 'mode': 'TAXI'},

        # Día 5
        {'start': 'IMG_3747.JPG', 'end': 'IMG_6134.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_6134.JPG', 'end': 'IMG_METHARLEN.JPG', 'color': 'yellow', 'mode': 'METRO'},
        {'start': 'IMG_METHARLEN.JPG', 'end': 'IMG_3791.JPG', 'color': 'red', 'mode': 'ANDANDO'},

        # Día 6
        {'start': 'IMG_LASTNY.JPG', 'end': 'IMG_RENT_CAR.JPG', 'color': 'brown', 'mode': 'TAXI'},
        {'start': 'IMG_RENT_CAR.JPG', 'end': 'IMG_6257.JPG', 'color': 'blue', 'mode': 'COCHE'},
        {'start': 'IMG_6257.JPG', 'end': 'IMG_3815.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_3815.JPG', 'end': 'IMG_CABALLEROS.JPG', 'color': 'blue', 'mode': 'COCHE'},

        # Día 7
        {'start': 'IMG_3817.JPG', 'end': 'IMG_6360.JPG', 'color': 'blue', 'mode': 'COCHE'},
        {'start': 'IMG_6360.JPG', 'end': 'IMG_3885.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_3885.JPG', 'end': 'IMG_TOLEDO.JPG', 'color': 'blue', 'mode': 'COCHE'},

        # Día 8
        {'start': 'IMG_6440.JPG', 'end': 'IMG_HOTCHI.JPG', 'color': 'blue', 'mode': 'COCHE'},
        {'start': 'IMG_HOTCHI.JPG', 'end': 'IMG_6500.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_6500.JPG', 'end': 'IMG_6511.JPG', 'color': 'yellow', 'mode': 'METRO'},
        {'start': 'IMG_6511.JPG', 'end': 'IMG_6612.JPG', 'color': 'red', 'mode': 'ANDANDO'},
        {'start': 'IMG_6612.JPG', 'end': 'IMG_HOTCHIC.JPG', 'color': 'brown', 'mode': 'TAXI'}
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
        start_idx = get_index(df, segment['start'])
        end_idx = get_index(df, segment['end'])
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
                <span style='color: red;'>■</span> Andando<br>
                <span style='color: blue;'>■</span> Coche<br>
                <span style='color: pink;'>■</span> Avión<br>
                <span style='color: brown;'>■</span> Taxi<br>
                <span style='color: yellow;'>■</span> Metro<br>
                <span style='color: green;'>■</span> Tren<br>
                <span style='color: lightblue;'>■</span> Ferry<br>
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
