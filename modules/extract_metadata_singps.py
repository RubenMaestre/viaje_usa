import os
import pandas as pd
import exifread

def get_exif_data(image_path):
    with open(image_path, 'rb') as img_file:
        tags = exifread.process_file(img_file)
        exif_data = {
            "file_name": os.path.basename(image_path),
            "date_time": None,
        }

        # Extraer la fecha si está disponible
        date_time_original = tags.get("EXIF DateTimeOriginal")

        if date_time_original:
            exif_data["date_time"] = str(date_time_original)

    return exif_data

def process_files(folder):
    files = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    data_list = []

    for file in files:
        file_path = os.path.join(folder, file)
        data = get_exif_data(file_path)
        data_list.append(data)

    return data_list

def create_metadata_df(folder_path):
    data_list = process_files(folder_path)
    df = pd.DataFrame(data_list)
    return df

# Ruta de la carpeta de fotos sin coordenadas GPS
folder_path = 'C:/Users/34670/Desktop/python/coast_to_coast/viaje_usa/fotos_usa_13'

# Crear el DataFrame
df_fotos_videos = create_metadata_df(folder_path)

# Guardar el DataFrame como un archivo CSV para usarlo en la aplicación
df_fotos_videos.to_csv('C:/Users/34670/Desktop/python/coast_to_coast/viaje_usa/data/metadata_singps.csv', index=False)
