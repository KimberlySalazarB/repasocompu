#Asincronía con asyncio
#Escribe un script que utilice asyncio para realizar peticiones
# HTTP asincrónicas a tres APIs diferentes y recolecte sus respuestas.

import aiohttp
import asyncio

async def fetch(session, url):
    """Función asincrónica para realizar una petición HTTP."""
    async with session.get(url) as response:
        return await response.text()

async def main():
    """Función principal que coordina las peticiones HTTP asincrónicas."""
    urls = [
        'https://api.github.com',  # GitHub API para metadatos
        'https://api.ipify.org?format=json',  # API para obtener la IP pública
        'https://jsonplaceholder.typicode.com/todos/1'  # API de ejemplo de JSONPlaceholder
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)

        for response in responses:
            print(response)

# Obtener el bucle de eventos existente y ejecutar la función principal
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
except RuntimeError:
    asyncio.run(main())  # Solo para casos donde el primer método falla (como ejecución fuera de notebook)

############################################################################
#para notebook
import aiohttp
import asyncio
import nest_asyncio

nest_asyncio.apply()  # Aplica parche a asyncio para permitir anidamiento de bucles

async def fetch(session, url):
    """Función asincrónica para realizar una petición HTTP."""
    async with session.get(url) as response:
        return await response.text()

async def main():
    """Función principal que coordina las peticiones HTTP asincrónicas."""
    urls = [
        'https://api.github.com',  # GitHub API para metadatos
        'https://api.ipify.org?format=json',  # API para obtener la IP pública
        'https://jsonplaceholder.typicode.com/todos/1'  # API de ejemplo de JSONPlaceholder
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)

        for response in responses:
            print(response)

# Ejecutar el script en un entorno con un bucle de eventos ya en ejecución
asyncio.run(main())