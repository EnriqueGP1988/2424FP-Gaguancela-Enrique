# Crear una matriz 3D que represente los datos de temperaturas diarias de 3 ciudades.
# En una dimensión, puedes tener diferentes ciudades.
# En otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.).
# En la tercera dimensión, semanas.

temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 24}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 28}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 16}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 22}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Riobamba", "Ambato", "Quito"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"El promedio de temperatura en la ciudad de {ciudades[ciudad_idx]}, en la Semana {semana_idx + 1}: es de {promedio:.2f} ° C")