#Uso de asyncio con manejo de excepciones
#Desarrolla un script utilizando asyncio que realice peticiones HTTP a
#varios endpoints. Utiliza manejo de excepciones para tratar adecuadamente
# los errores de conexión y otros errores HTTP.

import aiohttp
import asyncio

async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.text()
                print(f"Respuesta exitosa de {url}: {data[:100]}...")  # Imprime los primeros 100 caracteres
            else:
                print(f"Error {response.status} desde {url}")
    except aiohttp.ClientConnectionError:
        print(f"Error de conexión con {url}")
    except aiohttp.ClientError as e:
        print(f"Error al realizar la petición a {url}: {e}")

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)

# Ejecuta directamente la función main con await en Jupyter
if __name__ == "__main__":
    urls = [
        "http://example.com",
        "http://nonexistent.url",
        "http://httpbin.org/status/404",
        "http://httpbin.org/status/500"
    ]
    
    # Directamente usar await aquí si es una celda de Jupyter
    await main(urls)
    #Desde .py 
    #asyncio.run(main(urls))