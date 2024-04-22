# modules/map/etapa_1.py
import folium

def create_map():
    start_coords = (40.7127281, -74.0060152)  # Nueva York
    end_coords = (41.3571604455432, -71.9677955522056)  # Mystic River

    # Crear un mapa centrado en las coordenadas de inicio
    map = folium.Map(location=start_coords, zoom_start=8)

    # Añadir un marcador para el punto de inicio
    folium.Marker(start_coords, popup='Inicio: Nueva York').add_to(map)

    # Añadir un marcador para el punto de destino
    folium.Marker(end_coords, popup='Destino: Mystic River').add_to(map)

    # Dibujar una línea entre el punto de inicio y el destino
    folium.PolyLine([start_coords, end_coords], color='blue', weight=2.5, opacity=1).add_to(map)
    
    # Devolver el objeto mapa para ser usado en streamlit
    return map