from functools import reduce #importante para usar reduce

def to_upper(word):
    # upper -> convierte una palabra en mayuscula
    # lower -> convierte una palabra a minusculas
    return word.upper()

def concatenate(a, b):
    # concatenar dos cadenas -> reduce
    return a + ',' + b

def main():
    words = ["hello", "world", "this", "is", "python"]
    
    # usar map para convertir todas las palabras en mayusculas
    upper_words = map(to_upper, words)
    
    # usar reduce para concatenarlas en una sola cadena 
    concatenated_string = reduce(concatenate, upper_words)
    
    print(concatenated_string)

if __name__ == "__main__":
    main()
        
########################################################
def main():
    words = ['hola', 'mundo', 'programación', 'funcional', 'Python']
    # Convertir todas las palabras a mayúsculas
    # upper -> convierte una palabra en mayuscula
    # lower -> convierte una palabra a minusculas
    # capitalize -> solo la primera letra en mayuscula
    #swapcase -> cambiar mayusculas por minusculas y viceversa 
    upper_words = map(str.upper, words)
    
    # Concatenar todas las palabras en una cadena separada por comas usando un bucle for
    result = ""
    for word in upper_words:
        if result:  # Si result ya tiene contenido, añadimos una coma antes del siguiente elemento
            result += ","
        result += word

    print(result)

if __name__ == '__main__':
    main()