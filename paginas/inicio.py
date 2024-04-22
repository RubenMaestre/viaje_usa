# paginas/inicio.py
import streamlit as st

def display():
    # Imagen de cabecera (si decides volver a incluirla)
    # st.image('sources/cabecera.jpg', use_column_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)  # Espacio extra

    # Título de la página
    st.markdown("<h1 style='text-align: center;'>Coast to Coast - USA</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Introducción descriptiva
    st.markdown("""
        <div style='text-align: justify;'>
            Bienvenidos a este proyecto a modo de recuerdo de lo que fue para mí sin duda uno de los viajes
            más inolvidables que he realizado en mi vida. Y gracias a la tecnología de Streamlit para plasmar
            los datos, coordenadas y demás, quiero compartir con vosotros aquellos bonitos recuerdos.
        </div>
        """, unsafe_allow_html=True)
