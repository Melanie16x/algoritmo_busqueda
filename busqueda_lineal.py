# Funcion para la busqueda lineal
def busqueda_lineal(lista, elemento):
    # bucle que busca el elemento en la lista
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i  # Retorna el índice del elemento encontrado
    return -1  # Retorna -1 si el elemento no está en la lista

# Ejemplo para la prueba
lista = [3, 5, 2, 4, 9]
elemento_buscado = 4
resultado = busqueda_lineal(lista, elemento_buscado)

# Condicion que imprime un mensaje dependiendo del resultado de la funcion
if (resultado == -1):
    print("El elemento buscado no se encuentra en la lista.")
else:
    print("Elemento encontrado en el índice:", resultado)
