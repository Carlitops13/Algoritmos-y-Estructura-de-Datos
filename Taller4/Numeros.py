
# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor); imprimir el orden de los números
numero_uno= int(input("Ingrese el primer numero: "))
numero_dos= int(input("Ingrese el segundo numero: "))
numero_tres= int(input("Ingrese el tercer numero: "))

if numero_uno > numero_dos and numero_uno>numero_tres:
    if numero_dos>numero_tres:
        print("El orden de los números es: ", numero_uno, numero_dos, numero_tres)
    else:
        print("El orden de los números es: ", numero_uno, numero_tres, numero_dos)
elif numero_dos>numero_uno and numero_dos>numero_tres:
    if numero_uno>numero_tres:
        print("El orden de los números es: ", numero_dos, numero_uno, numero_tres)
    else:
        print("El orden de los números es: ", numero_dos, numero_tres, numero_uno)
elif numero_tres>numero_uno and numero_tres>numero_dos:
     if numero_uno>numero_dos:
        print("El orden de los números es: ", numero_tres, numero_uno, numero_dos)
     else:
        print("El orden de los números es: ", numero_tres, numero_dos, numero_uno)
elif numero_uno==numero_dos and numero_uno>numero_tres:
     if numero_dos>numero_tres:
        print("El orden de los números es: ", numero_uno, numero_dos, numero_tres)
     else:
        print("El orden de los números es: ", numero_uno, numero_tres, numero_dos)
elif numero_uno==numero_tres and numero_uno>numero_dos:
    if numero_dos>numero_tres:
        print("El orden de los números es: ", numero_uno, numero_dos, numero_tres)
    else:
        print("El orden de los números es: ", numero_uno, numero_tres, numero_dos)
elif numero_dos==numero_tres and numero_dos>numero_uno:
    if numero_uno>numero_tres:
        print("El orden de los números es: ", numero_dos, numero_uno, numero_tres)
    else:
        print("El orden de los números es: ", numero_dos, numero_tres, numero_uno)
elif numero_uno==numero_dos and numero_uno==numero_tres:
    print("Los números son iguales")

