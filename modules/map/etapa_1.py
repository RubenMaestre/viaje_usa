import folium
from folium.plugins import BeautifyIcon

def create_map():
    start_coords = (40.7127281, -74.0060152)  # Nueva York
    end_coords = (41.3571604455432, -71.9677955522056)  # Mystic River
    
    # Crear un mapa centrado en las coordenadas de inicio
    map = folium.Map(location=start_coords, zoom_start=10)

    # Añadir un marcador para el punto de inicio y un pop-up
    folium.Marker(
        start_coords,
        popup='Inicio: Nueva York',
        icon=BeautifyIcon(icon='play', prefix='fa')
    ).add_to(map)

    # Añadir un marcador para el punto de destino y un pop-up
    folium.Marker(
        end_coords,
        popup='Destino: Mystic River',
        icon=BeautifyIcon(icon='flag', prefix='fa')
    ).add_to(map)
    
    # Dibujar la ruta entre el punto de inicio y el destino (esto será una línea recta, para una ruta específica necesitarás una API de routing)
    folium.PolyLine([start_coords, end_coords], color='blue', weight=2.5, opacity=1).add_to(map)
    
    return map