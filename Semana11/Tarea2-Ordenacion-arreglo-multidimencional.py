# Ordenación de Arreglo Multidimensional
# Escribe un programa que incluya una matriz bidimensional con valores numéricos (puede ser una matriz pequeña de 3x3).
# Implementa una función que ordene una fila específica de la matriz en orden ascendente utilizando un algoritmo de ordenación de tu elección (por ejemplo, Bubble Sort o QuickSort).
# Muestra la matriz original y la matriz con la fila ordenada.

# Creación de la matriz bidimensional (3x3).
matriz = [
    [1, 4, 9],
    [6, 5, 2],
    [7, 8, 3]
]

# Ordenar una fila de manera ascendente (Bubble Sort).
def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambio de elementos.

# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Visualizar la matriz original.
print("La matriz original es:")
mostrar_matriz(matriz)

# Ordenar cada fila de la matriz (Bubble Sort).
for fila in matriz:
    bubble_sort_fila(fila)

# Visualizar la matriz ordenada.
print("\nLa matriz ordenada ascendentemente por filas es:")
mostrar_matriz(matriz)
