# paginas/preparativos.py
import streamlit as st

def display():
    st.markdown("<br><br>", unsafe_allow_html=True)  # Espacio extra

    # Título de la página
    st.markdown("<h1 style='text-align: center;'>Preparativos</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Imagen de preparativos
    st.image('sources/preparativos.jpg', use_column_width=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Texto introductorio
    st.markdown("""
        <div style='text-align: justify; font-size: 18px;'>
            Los preparativos para un viaje siempre están llenos de nervios y expectativas, especialmente cuando se trata de un viaje tan increíble como este. 
            Preparar la maleta, decidir qué llevar y estar listo para enfrentar diferentes zonas climáticas es todo un reto.
            <br><br>
            Salimos de Elche de madrugada con el coche para aparcar en el aeropuerto de Barajas. Desde allí, volamos a Londres, donde hicimos escala, 
            y luego al aeropuerto de Nueva York, el John F. Kennedy. Así arrancó esta gran aventura.
        </div>
    """, unsafe_allow_html=True)

# Llamar a la función display para mostrar la página
display()
