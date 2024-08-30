# Programa 1: Búsqueda en Arreglo Multidimensional
# Escribe un programa que incluya una matriz bidimensional
# (puede ser una matriz pequeña de 3x3) con valores numéricos.

matriz = [
    [6, 5, 4],
    [2, 9, 3],
    [7, 1, 8]
]

# Determinar el valor (número) que esta buscando.
valor_buscado = 5

# Inicializar variables para rastrear la posición del valor
fila_encon = -1
columna_encon = -1

# Buscar el valor en la matriz
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_encon = fila
            columna_encon = columna
            break  # Detener la búsqueda una vez que se ha encontrado el valor
    if fila_encon != -1:
        break  # Salir del bucle una vez que se ha encontrado el valor.

# Verificar si se encontró el valor y mostrar la posición dentro de la matriz.
if fila_encon != -1:
    print(f"El valor buscado: {valor_buscado} se encuentra en la fila {fila_encon} y columna {columna_encon}.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")
