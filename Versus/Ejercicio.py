#Ejercicio 1: La Caja Registradora 🛒
#Objetivo: Crear un programa que simule una caja registradora.

#El programa debe hacer lo siguiente:

#Preguntar al usuario cuántos productos va a registrar.
#Usando un bucle, pedir el precio de cada producto y guardarlos en una lista.
#Calcular y mostrar el subtotal (la suma de todos los precios).
#Si el subtotal supera los $100, se debe calcular y mostrar un descuento del 10%. Si no, el descuento es $0.
#Finalmente, mostrar el total a pagar (subtotal - descuento).
#Conceptos Clave a Demostrar:

# Entrada de datos con input().
# Conversión de tipos con int() y float().
# Uso de un bucle for con range().
# Manejo de listas, incluyendo crear una lista vacía y agregar elementos con .append().
# Lógica condicional con if/else.
# Operadores aritméticos para los cálculos.
# Recuerden los criterios: Funcionalidad (5 pts), Uso de Conceptos (3 pts) y Claridad del Código (2 pts).

from ast import Add


preciosIngresados = []  
subtotal = 0
descuento = 0
total = 0


num_productos = int(input("Ingrese la cantidad de productos a registrar: "))
for i in range(num_productos):
    precio = float(input("Ingrese el precio del producto: "))
    preciosIngresados.append(precio)
    subtotal += precio


if subtotal > 100:
    descuento = subtotal * 0.1


total = subtotal - descuento


print("El subtotal es: ", subtotal)
print("El descuento es: ", descuento)
print("El total a pagar es: ", total)
