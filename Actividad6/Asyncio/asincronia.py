import aiohttp
import asyncio
import nest_asyncio
#pip install nest_asyncio

# Aplica un parche a asyncio para permitir anidamiento de bucles de eventos.
nest_asyncio.apply()

async def fetch(session, url):
    """
    Función asincrónica para realizar una petición HTTP.
    """
    async with session.get(url) as response:
        # Espera a recibir la respuesta completa y retorna el texto.
        return await response.text()

async def main():
    """
    Función principal que coordina las peticiones HTTP asincrónicas.
    """
    urls = [
        'https://api.github.com',  # GitHub API para metadatos
        'https://api.ipify.org?format=json',  # API para obtener la IP pública
        'https://jsonplaceholder.typicode.com/todos/1'  # API de ejemplo de JSONPlaceholder
    ]

    # Crear una sesión de cliente aiohttp para realizar peticiones HTTP.
    async with aiohttp.ClientSession() as session:
        # Crear una lista de tareas de fetch para cada URL.
        tasks = [fetch(session, url) for url in urls]
        # Ejecutar todas las tareas de forma asincrónica y esperar a que todas finalicen.
        responses = await asyncio.gather(*tasks)

        # Imprimir las respuestas obtenidas.
        for response in responses:
            print(response)

# Ejecutar el script en un entorno con un bucle de eventos ya en ejecución.
asyncio.run(main())

##############################################################
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()  # Parse JSON response

async def main():
    urls = [
        'https://jsonplaceholder.typicode.com/todos/1',
        'https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&current_weather=true',
        'https://httpbin.org/delay/2'  # This endpoint introduces a delay of 2 seconds
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

