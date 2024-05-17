import os
import requests
from concurrent.futures import ThreadPoolExecutor

# Lista de URLs de las imágenes que deseamos descargar
image_urls = [
    "https://img.freepik.com/psd-gratis/hermoso-gato-retrato-aislado_23-2150186184.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/June_odd-eyed-cat.jpg/220px-June_odd-eyed-cat.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Hawthorne_Bridge%2C_Portland%2C_Oregon_%282018%29_-_2.jpg/320px-Hawthorne_Bridge%2C_Portland%2C_Oregon_%282018%29_-_2.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/NYC_Midtown_Skyline_at_night_-_Jan_2006_edit1.jpg/320px-NYC_Midtown_Skyline_at_night_-_Jan_2006_edit1.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Tulip_-_floriade_canberra.jpg/320px-Tulip_-_floriade_canberra.jpg"
]


def download_image(url):
    """Función para descargar una imagen y guardarla localmente."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Asegura que la respuesta fue exitosa

        # Extraer nombre de archivo de la URL
        file_name = os.path.basename(url)
        
        # Guardar el archivo en el directorio actual
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print(f"Descarga completada: {file_name}")
    except requests.RequestException as e:
        print(f"Error al descargar {url}: {e}")

def main():
    # Usar un ThreadPoolExecutor para descargar imágenes en paralelo
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_image, image_urls)

if __name__ == "__main__":
    main()