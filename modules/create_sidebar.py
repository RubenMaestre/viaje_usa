# modules/create_sidebar.py
import streamlit as st
from paginas import preparativos
from streamlit_option_menu import option_menu
from paginas import inicio, preparativos, ruta

def create_sidebar():
    # Añadir texto personalizado en el sidebar con markdown y HTML
    st.sidebar.markdown(
        f'<div style="text-align: center; font-size: 18px; margin-bottom: 30px;">'
        f'Proyecto realizado por<br>'
        f'Rubén Maestre'
        f'</div>',
        unsafe_allow_html=True
    )

    # Crear el menú de opciones en el sidebar con option_menu
    with st.sidebar:
        selected = option_menu("Menú", ["Inicio", "Preparativos", "Ruta"],
            icons=["house", "bagage", "map"],
            menu_icon="cast", default_index=0, orientation="vertical")

    # Llama a la función de la página correspondiente en función de la selección
    if selected == "Inicio":
        inicio.display()
    elif selected == "Preparativos":
        preparativos.display()
    elif selected == "Ruta":
        ruta.display()

