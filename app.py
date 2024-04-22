# app.py
from modules.config_page import set_global_page_config
import streamlit as st

# Llama a set_page_config al inicio y asegúrate de que es el primer comando de Streamlit usado en el script.
set_global_page_config()

# Importaciones adicionales y lógica de la aplicación aquí
from modules.create_sidebar import create_sidebar

# Otros comandos de Streamlit y funciones deben ir después de set_page_config()
create_sidebar()


