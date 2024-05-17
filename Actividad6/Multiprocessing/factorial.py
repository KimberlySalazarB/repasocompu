import multiprocessing

#factorial

def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return (numero, factorial)

#paralelismo    
def map_test():
    pool = multiprocessing.Pool()
    
    inputs = [5, 7, 9]
    ouputs = pool.map(calcular_factorial, inputs)
    print(ouputs)

map_test()


##############################################################
import multiprocessing

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result

def compute_factorial(number, result_dict):
    # Calcular el factorial y almacenarlo en un diccionario compartido.
    result_dict[number] = factorial(number)
    print(f"El factorial de {number} es {result_dict[number]}")

if __name__ == '__main__':
    # Lista de números para los cuales queremos calcular el factorial.
    numbers = [5, 7, 9]
    
    # Diccionario que se usa para almacenar los resultados.
    # Utilizamos un Manager dict para permitir el acceso entre procesos.
    manager = multiprocessing.Manager()
    result_dict = manager.dict()
    
    # Lista para mantener los procesos.
    processes = []
    
    # Crear y lanzar un proceso por cada número.
    for number in numbers:
        # Creamos el proceso.
        process = multiprocessing.Process(target=compute_factorial, args=(number, result_dict))
        
        # Añadimos el proceso a la lista de procesos.
        processes.append(process)
        
        # Iniciar el proceso.
        process.start()
    
    # Esperar a que todos los procesos terminen.
    for process in processes:
        process.join()
    
    print("Todos los procesos terminados.")
    

