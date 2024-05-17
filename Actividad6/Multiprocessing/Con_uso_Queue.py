#Multiprocessing con uso de Queue para intercambio de datos
#Implementa un programa que use multiprocessing donde varios 
#procesos productores generan números aleatorios y un consumidor 
#los suma. Usa Queue para la comunicación entre procesos.

import multiprocessing
import random
import time

def producer(queue):
    """ Función que simula un productor de números aleatorios. """
    for _ in range(10):
        num = random.randint(1, 100)
        queue.put(num)
        print(f"Producido {num}")
        time.sleep(random.random())
    # Indicar que la producción ha terminado
    queue.put(None)

def consumer(queue, num_producers):
    """ Función que simula un consumidor que suma los números recibidos. """
    total_sum = 0
    termination_count = 0
    
    while True:
        num = queue.get()
        if num is None:
            termination_count += 1
            if termination_count == num_producers:
                break
        else:
            total_sum += num
            print(f"Consumido {num}, la suma total es ahora {total_sum}")
    
    print(f"La suma final es {total_sum}")

def main():
    # Número de procesos productores
    num_producers = 3
    
    # Crear una cola para comunicar números entre productores y consumidor
    queue = multiprocessing.Queue()
    
    # Crear y comenzar los procesos productores
    producers = [multiprocessing.Process(target=producer, args=(queue,)) for _ in range(num_producers)]
    for p in producers:
        p.start()
    
    # Crear y comenzar el proceso consumidor
    consumer_process = multiprocessing.Process(target=consumer, args=(queue, num_producers))
    consumer_process.start()
    
    # Esperar a que todos los procesos productores terminen
    for p in producers:
        p.join()
    
    # Esperar a que el proceso consumidor termine
    consumer_process.join()

if __name__ == "__main__":
    main()