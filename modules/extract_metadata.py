# modules/extract_metadata.py
import os
import pandas as pd
import exifread
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from fractions import Fraction

def get_exif_data(image_path):
    with open(image_path, 'rb') as img_file:
        tags = exifread.process_file(img_file)
        exif_data = {
            "file_name": os.path.basename(image_path),
            "latitude": None,
            "longitude": None,
            "altitude": None,
            "date_time": None,
        }

        # Extract GPS data if available
        gps_latitude = tags.get("GPS GPSLatitude")
        gps_latitude_ref = tags.get("GPS GPSLatitudeRef")
        gps_longitude = tags.get("GPS GPSLongitude")
        gps_longitude_ref = tags.get("GPS GPSLongitudeRef")
        gps_altitude = tags.get("GPS GPSAltitude")
        date_time_original = tags.get("EXIF DateTimeOriginal")

        def convert_to_degrees(value):
            parts = str(value).strip('[]').replace(' ', '').split(',')
            d = float(Fraction(parts[0]))
            m = float(Fraction(parts[1]))
            s = float(Fraction(parts[2]))
            return d + (m / 60.0) + (s / 3600.0)

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = convert_to_degrees(gps_latitude)
            lon = convert_to_degrees(gps_longitude)

            exif_data["latitude"] = lat * (-1 if gps_latitude_ref.values[0] == 'S' else 1)
            exif_data["longitude"] = lon * (-1 if gps_longitude_ref.values[0] == 'W' else 1)
        
        if gps_altitude:
            exif_data["altitude"] = float(gps_altitude.values[0])

        if date_time_original:
            exif_data["date_time"] = str(date_time_original)

    return exif_data

def get_video_metadata(video_path):
    parser = createParser(video_path)
    metadata = extractMetadata(parser)
    video_data = {
        "file_name": os.path.basename(video_path),
        "latitude": None,
        "longitude": None,
        "altitude": None,
        "date_time": None,
    }

    if metadata:
        for item in metadata.exportPlaintext():
            if "Creation date" in item:
                video_data["date_time"] = item.split(": ")[1].strip()
            if "GPS coordinates" in item:
                coords = item.split(": ")[1].strip().split(", ")
                lat, lon = coords[0].split(" "), coords[1].split(" ")
                video_data["latitude"] = float(lat[0]) * (-1 if lat[1] == 'S' else 1)
                video_data["longitude"] = float(lon[0]) * (-1 if lon[1] == 'W' else 1)

    return video_data

def process_files(folder):
    files = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.mov'))]
    data_list = []

    for file in files:
        file_path = os.path.join(folder, file)
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            data = get_exif_data(file_path)
        elif file.lower().endswith('.mov'):
            data = get_video_metadata(file_path)
        data_list.append(data)

    return data_list

def create_metadata_df(folder_path):
    data_list = process_files(folder_path)
    df = pd.DataFrame(data_list)
    return df

# Ruta de la carpeta de fotos y videos
folder_path = 'C:/Users/34670/Desktop/python/coast_to_coast/viaje_usa/fotos_usa'

# Crear el DataFrame
df_fotos_videos = create_metadata_df(folder_path)

# Guardar el DataFrame como un archivo CSV para usarlo en la aplicación
df_fotos_videos.to_csv('C:/Users/34670/Desktop/python/coast_to_coast/viaje_usa/data/metadata.csv', index=False)
