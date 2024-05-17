import asyncio

async def clock():
    for second in range(1, 11):  # Iterar de 1 a 10 segundos
        print(f"{second} segundo{'s' if second > 1 else ''} han pasado")
        await asyncio.sleep(1)  # Espera un segundo

# Código ajustado para un entorno con bucle de eventos en ejecución
async def main():
    await clock()  # Ejecutar la corutina del reloj

# Utilizar get_event_loop para obtener el bucle de eventos actual
loop = asyncio.get_event_loop()

# Verificar si el bucle de eventos está en ejecución
if loop.is_running():
    # Ejecutar la corutina en el bucle de eventos ya existente
    asyncio.ensure_future(main())
else:
    # Iniciar el bucle de eventos y correr la corutina
    loop.run_until_complete(main())