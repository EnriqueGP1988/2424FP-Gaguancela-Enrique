# Creación de la función (calcular_descuento).

def calcular_descuento (monto_total, descuento = 10):
    # Cáñculo del porcentaje de descuento
    total_descuento = (descuento / 100) * monto_total
    return total_descuento

# Código de las operaciones a realizar.

# Primera llamada con una compra de tres productos y un descuento del 10%
print('---PRIMERA COMPRA---')
producto1 = float(input("ingrese el valor del primer producto: $"))
producto2 = float(input("ingrese el valor del segundo producto: $"))
producto3 = float(input("ingrese el valor del tercer producto: $"))
monto_total_1 = producto1 + producto2 + producto3
total_descuento_1 = calcular_descuento (monto_total_1)
total_pagar_1 = monto_total_1 - total_descuento_1

# Impresión de los valores correspondientes a la primera compra
print (f'*******El valor total de la primera compra es de: ${monto_total_1}*******')
print (f'*******Descuento 10%: ${total_descuento_1}*******')
print (f'*******El valor total a pagar es de: ${total_pagar_1}*******')

print()
print()
print('---SEGUNDA COMPRA---')

# Segunda llamada con una compra de tres productos y un descuento del 20%
producto4 = float(input("ingrese el valor del primer producto: $"))
producto5 = float(input("ingrese el valor del segundo producto: $"))
producto6 = float(input("ingrese el valor del tercer producto: $"))
monto_total_2 = producto4 + producto5 + producto6
descuento_2 = 20
descuento_compra_2 = calcular_descuento (monto_total_2, descuento_2)
total_pagar_2 = monto_total_2 - descuento_compra_2

# Impresión de los valores correspondientes a la segunda compra
print (f'*******El valor total de la segunda compra es de: ${monto_total_2}*******')
print (f'*******Descuento 20%: ${descuento_compra_2}*******')
print (f'*******El valor total a pagar es de: ${total_pagar_2}*******')