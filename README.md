# Algoritmos_busqueda

## Búsqueda Lineal

La búsqueda lineal es un algoritmo sencillo que revisa cada elemento de la lista secuencialmente hasta encontrar el elemento buscado o llegar al final de la lista.

### Funcionamiento:

1. Comienza en el primer elemento de la lista.
2. Compara el elemento actual con el elemento buscado.
3. Si el elemento es encontrado, se devuelve su índice.
4. Si no es encontrado y se ha llegado al final de la lista, se devuelve un valor que indique que no se encontró (por ejemplo, -1).

## Busqueda Binaria

La búsqueda binaria es un algoritmo más eficiente que la búsqueda lineal, pero requiere que la lista esté ordenada previamente.

### Funcionamiento:

1. Comienza comparando el elemento medio de la lista con el elemento buscado.
2. Si el elemento buscado es igual al elemento medio, se devuelve su índice.
3. Si el elemento buscado es menor que el elemento medio, se repite el proceso con la sublista de la izquierda.
4. Si el elemento buscado es mayor que el elemento medio, se repite el proceso con la sublista de la derecha.
5. Este proceso se repite hasta encontrar el elemento o reducir la sublista a tamaño cero.
