# paginas/inicio.py
import streamlit as st
from streamlit_folium import folium_static

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
            .intro-text {
                text-align: justify;
                font-size: 18px;
            }
        </style>
        <h1>Coast to Coast - USA</h1>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Crear columnas
    col1, col2, col3 = st.columns([1.8, 0.2, 3])

    with col1:
        # Introducción descriptiva y explicación del proyecto
        st.markdown("""
            <div class='intro-text'>
                Bienvenidos a este proyecto a modo de recuerdo de lo que fue para mí sin duda uno de los viajes más inolvidables que he realizado en mi vida. Entre el 28 de julio de 2013 y el 15 de agosto de 2013, recorrimos Estados Unidos desde Nueva York hasta San Francisco en coche. Este viaje fue una experiencia única y llena de aventuras que ahora puedo compartir gracias a la tecnología.
                <br><br>
                Gracias a las fotos almacenadas en mi iPhone, he podido extraer las coordenadas de cada una y trazar la ruta exacta que seguimos. Cada marcador en el mapa representa una parada, una vista espectacular o un momento especial capturado durante este emocionante recorrido. Espero que disfruten este viaje virtual tanto como yo disfruté haciéndolo.
                <br><br>
                Además de la parte sentimental y de recuerdo, este proyecto también busca explorar nuevas opciones en el análisis y extracción de datos. He sacado la información de las fotos del iPhone para extraer coordenadas y también estoy trabajando en sacar la información de fotos realizadas con una CANON EOS 1100, que no tienen coordenadas.
                <br><br>
                He tenido que adaptar las horas de las fotos a las horas de Estados Unidos, que tiene 4 husos horarios diferentes, porque la cámara estaba configurada para el horario de Madrid. Con todo ello, estoy trabajando de diferentes formas: relacionando coordenadas de fotos del iPhone con las de la Canon en la misma línea temporal, utilizando aplicaciones como geospy.ai, consultando con ChatGPT, y usando Google Maps.
                <br><br>
                La primera parte del proyecto consiste en poner las coordenadas de todas las fotos y graficarlas por rutas en Folium. También he trazado líneas indicando si vamos andando, en coche, en tren, en ferry, avión, etc. A partir de ahí, trabajaré en otras métricas como el número total de kilómetros, ciudades visitadas, estados, y otras curiosidades.
                <br><br>
                Por último, incluiré en los mapas las fotografías de los lugares más bonitos o especiales, ilustrando el viaje con imágenes significativas.
                <br><br>
                En definitiva, este es un proyecto diferente, creativo y original en Streamlit, al cual estoy dedicando muchas horas de programación y práctica con nuevas herramientas. Espero que disfrutéis de la página tanto como yo estoy disfrutando montándola.
            </div>
        """, unsafe_allow_html=True)

    with col3:
        # Imagen del proyecto
        st.image('sources/coast_to_coast.jpg', use_column_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

# Llamar a la función display para mostrar la página
display()
