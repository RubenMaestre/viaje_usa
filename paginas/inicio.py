# paginas/inicio.py
import streamlit as st
from modules.map.etapa_1 import draw_route_osmnx

def display():
    font_link = "https://fonts.googleapis.com/css2?family=Roboto:wght@100;400;700&display=swap"
    st.markdown(f"<link href='{font_link}' rel='stylesheet'>", unsafe_allow_html=True)

    # Usando la fuente en un elemento HTML
    st.markdown("""
        <style>
            h1 {
                font-family: 'Roboto', sans-serif;
                text-align: center;
            }
        </style>
        <h1>Coast to Coast - USA</h1>
    """, unsafe_allow_html=True)
    st.image('sources/coast_to_coast.jpg', use_column_width=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Introducción descriptiva
    st.markdown("""
        <div style='text-align: justify;'>
            Bienvenidos a este proyecto a modo de recuerdo de lo que fue para mí sin duda uno de los viajes
            más inolvidables que he realizado en mi vida. Y gracias a la tecnología de Streamlit para plasmar
            los datos, coordenadas y demás, quiero compartir con vosotros aquellos bonitos recuerdos.
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)  # Espacio extra

    image_path = draw_route_osmnx()

    # Mostrar la imagen en Streamlit
    st.image(image_path, use_column_width=True)