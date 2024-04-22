# modules/map/etapa_1.py
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# Función para calcular y dibujar la ruta usando osmnx
def draw_route_osmnx():
    # Coordenadas de inicio y destino dentro de la función
    start_lat, start_lon = 40.7127281, -74.0060152  # Nueva York
    end_lat, end_lon = 41.3571604455432, -71.9677955522056  # Mystic River
    ox.config(use_cache=True, log_console=True)
    ox.settings.network_type = 'drive'

    # Obtener la red de carreteras para el área alrededor de los puntos de inicio y fin
    G = ox.graph_from_point((start_lat, start_lon), dist=3000, dist_type='bbox', network_type='drive')
    G = nx.compose(G, ox.graph_from_point((end_lat, end_lon), dist=3000, dist_type='bbox', network_type='drive'))

    # Encontrar el nodo más cercano en la red para el inicio y el fin utilizando nearest_nodes
    start_node = ox.nearest_nodes(G, start_lon, start_lat)
    end_node = ox.nearest_nodes(G, end_lon, end_lat)

    # Calcular la ruta más corta
    route = nx.shortest_path(G, start_node, end_node, weight='length')

    # Asegúrate de definir la figura y el eje antes de plotear
    fig, ax = ox.plot_graph(G, show=False, close=False, edge_color='black', node_size=0)
    ox.plot_graph_route(G, route, route_color='blue', route_linewidth=6, ax=ax)
    
     # Guardar la imagen en un archivo en lugar de mostrarla con plt.show()
    image_filepath = '/mnt/data/route_image.png'
    fig.savefig(image_filepath, bbox_inches='tight')
    plt.close(fig)  # Cerrar la figura para liberar memoria
    
    # Devolver la ruta de la imagen para usar en Streamlit
    return image_filepath
