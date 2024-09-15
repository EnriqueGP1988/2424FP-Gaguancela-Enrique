# Desarrollar una función en Python que calcule
# La temperatura promedio de una ciudad durante un período de tiempo.
# La función debe ser capaz de manejar datos de temperaturas de múltiples
# ciudades y semanas.

# Crear función (promedio_temperatura).
# Comando def: sirve para definir funciones.

def promedio_temperatura(ciudades):

    promedio_temperatura = {}

    for ciudad, temperaturas in ciudades.items():
        promedio = sum(temperaturas) / len(temperaturas)
        promedio_temperatura[ciudad] = promedio

    # Comando return: retorna los valores
    return promedio_temperatura


# Módulo de 5 ciudades con 7 temperaturas (semana).
ciudades = {
    "Riobamba ": [24, 17, 30, 19, 28, 18, 25],
    "Ambato   ": [16, 16, 28, 27, 18, 22, 26],
    "Quito    ": [16, 30, 12, 18, 19, 30, 28],
    "Guayaquil": [27, 30, 26, 29, 30, 27, 28],
    "Cuenca   ": [21, 13, 17, 24, 11, 23, 30]
}

# Utilizamos la función (promedio_temperatura)
# para calcular las temperatura promedio de cada ciudad
temperaturas_promedio = promedio_temperatura(ciudades)

# Impresión de la ciudad con su respetivo promedio de temperatura.
print("El promedio de temperatura por cada ciudad es:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f}°C")