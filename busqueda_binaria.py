# Funcion para la busqueda binaria
def busqueda_binaria(lista, elemento):
    # Inicializa los limites izquierdo y derecho de la busqueda
    izquierda = 0
    derecha = len(lista) - 1
    
    # Bucle que evalua: Mientras el limite izquierdo no supere al derecho
    while izquierda <= derecha:
        # Encuentra el indice medio de la lista actual
        medio = (izquierda + derecha) // 2

        # Condicion que evalua: Si el elemento en el indice medio es el buscado, retorna el indice
        if lista[medio] == elemento:
            return medio  # Retorna el índice del elemento encontrado
        
        # Si el elemento buscado es mayor que el elemento en el indice medio,
        # ajusta el limite izquierdo a la posicion medio + 1
        elif lista[medio] < elemento:
            izquierda = medio + 1

        # Si el elemento buscado es menor que el elemento en el indicie medio,
        # ajusta el limite derecho a la posicion medio - 1
        else:
            derecha = medio - 1
    
    return -1  # Retorna -1 si el elemento no está en la lista

# Ejemplo de uso
lista = [2, 3, 4, 5, 9]
elemento_buscado = 4
resultado = busqueda_binaria(lista, elemento_buscado)

# Condicion que imprime un mensaje dependiendo del resultado de la funcion
if (resultado == -1):
    print("El elemento buscado no se encuentra en la lista.")
else:
    print("Elemento encontrado en el índice:", resultado)

