import multiprocessing 

def f(x): #calcular el cuadrado de un numero
    return x*x

def main():
    x = range(1, 11)
    #creamos un Pool de procesos
    with multiprocessing.Pool() as pool:
        squares = pool.map(f, x)
        
    print("Cuadrados de los numeros del 1 al 10:")
    for x, square in zip(x, squares):
        print(f'El cuadrado de {x} es {square}')
if __name__ == '__main__':
    main()
#################################################
import multiprocessing

def square_number(n):
    return n * n

def main():
    numbers = range(1, 11)  # Lista de números del 1 al 10
    with multiprocessing.Pool() as pool:
        # map aplica la función 'square_number' a cada elemento de la lista 'numbers'
        results = pool.map(square_number, numbers)
        print(results)

if __name__ == '__main__':
    # Correr la función main si el script es ejecutado como principal
    main()