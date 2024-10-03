# CREAR UN DICCIONARIO
# Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una persona,
# incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".


# Crear diccionario informacion_personal, incluyendo las claves: nombre, edad, ciudad y profesión.
informacion_personal = {"nombre": "Enrique", "edad": 36, "ciudad": "Riobamba", "profesion": "artesano"}


# ACCEDER Y MODIFICAR VALORES
# Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
# Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona.

# Modificar el valor de ciudad por uno diferente.
informacion_personal["ciudad"] = "Quito"

# Modificar el valor profesión por uno diferente.
informacion_personal["profesion"] = "ingeniero"


# VERIFICAR EXISTENCIA DE CLAVES
# Verifica si la clave "telefono" existe en el diccionario.
# Si no existe, agrégala con un número de teléfono ficticio.

# Verificar si la clave "telefono" existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-7890"


# ELIMINAR UNA CLAVE
# Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.

# Eliminar clave edad.
informacion_personal.pop("edad")


# IMPRIMIR EL DICCIONARIO FINAL
# Imprime el diccionario resultante después de realizar todas las operaciones.

print(informacion_personal)