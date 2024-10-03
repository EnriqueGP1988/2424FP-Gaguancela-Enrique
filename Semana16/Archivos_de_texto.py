# ESCRITURA DE ARCHIVO DE TEXTO
# Crea un nuevo archivo llamado my_notes.txt
# Escribe al menos tres líneas de notas personales en el archivo.


#Creación del archivo de texto my_notes.txt
my_notes = open("my_notes.txt", "w")

# Crear (escribir) tres líneas de información personal.
my_notes.write("ALUMNO: Enrique Gaguancela\n")
my_notes.write("CARRERA: Tecnologías de la Información\n")
my_notes.write("PAALELO: ***B***\n")



# LECTURA DE ARCHIVO DE TEXTO
# Abre el archivo my_notes.txt
# Lee el contenido del archivo línea por línea utilizando el método adecuado.
# Muestra en la consola cada línea leída.

# Abrir el archivo creado my_notes.txt
my_notes = open('my_notes.txt', 'r')

# Leer el contenido del archivo creado línea por línea.
# Impresión del encabezado
print("        INFORMACIÓN PERSONAL")
print("---------------------------------------")

# Utilización de la sentencia For para la Impresión de la información
# línea por línea.
for linea in my_notes.readlines():
    print(linea.rstrip('\n'))


# CIERRE DE ARCHIVOS
# Asegúrate de cerrar el archivo my_notes.txt después de realizar las operaciones
# necesarias.

# Cierre del archivo utilizado
my_notes.close()
