# modules/config_page.py
import streamlit as st

def set_global_page_config():
    st.set_page_config(
        page_title="Coast to Coast - Mi viaje en coche por USA",
        page_icon="us",
        layout="wide"
    )
