# paginas/ruta.py
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

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

    # Cargar el DataFrame con los metadatos desde el archivo Excel
    df = pd.read_csv('data/df_unido.csv')

    # Eliminar las dos primeras filas
    df = df.iloc[2:]

    # Filtrar filas con coordenadas no nulas
    df = df.dropna(subset=['latitude', 'longitude'])

    # Crear un mapa centrado en los EE. UU.
    map_center = [39.8283, -98.5795]
    map = folium.Map(location=map_center, zoom_start=4)

    # Añadir marcadores al mapa
    for idx, row in df.iterrows():
        # Determinar el color del marcador
        if idx == 2:
            color = 'red'  # Primer marcador
        elif idx == df.index[-1]:
            color = 'red'  # Último marcador
        else:
            color = 'blue'  # Otros marcadores
        
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"<b>{row['file_name']}</b><br>{row['date_time']}",
            icon=folium.Icon(color=color, icon='info-sign')
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
