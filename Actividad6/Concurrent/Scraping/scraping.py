import concurrent.futures
import requests
from bs4 import BeautifulSoup

#pip install requests beautifulsoup4

def fetch_and_parse(url):
    """
    Función que obtiene y parsea el contenido de una URL dada.
    """
    try:
        # Hacer la solicitud HTTP GET a la URL
        response = requests.get(url, timeout=10)
        # Verificar que la respuesta sea exitosa (status code 200)
        response.raise_for_status()
        # Parsear el contenido HTML de la página
        soup = BeautifulSoup(response.text, 'html.parser')
        # Buscar el primer tag <h1>
        title = soup.find('h1')
        # Si se encuentra un <h1>, retornar su texto; de lo contrario, indicar que no se encontró título
        if title:
            return (url, title.text.strip())
        else:
            return (url, 'No title found')
    except requests.RequestException as e:
        # En caso de error, retornar la URL y el mensaje de error
        return (url, f'Error fetching the page: {e}')

def main(urls):
    """
    Función principal que ejecuta tareas concurrentes.
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Ejecutar fetch_and_parse para cada URL en la lista usando ThreadPoolExecutor
        results = list(executor.map(fetch_and_parse, urls))
        
        # Imprimir los resultados
        for url, title in results:
            print(f'URL: {url}\nTitle: {title}\n')

if __name__ == "__main__":
    # Lista de URLs para hacer scraping
    urls = [
        "https://www.bbc.com",
        "https://www.cnn.com",
        "https://www.nytimes.com",
        "https://www.theguardian.com",
        "https://www.nbcnews.com"
    ]
    main(urls)

