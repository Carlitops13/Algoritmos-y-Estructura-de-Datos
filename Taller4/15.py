# 15.	Escribir un menú con la siguiente información:  (Use Match)
#1. Ingreso de datos
#2. Comprar
#3. Facturar
#4. Salir


print("Menú:")
print("1. Ingreso de datos")            
print("2. Comprar")
print("3. Facturar")
print("4. Salir")

opcion = int(input("Seleccione una opción: "))

match opcion:
    case 1:
        print("Ingreso de datos")
    case 2:
        print("Comprar")
    case 3:
        print("Facturar")
    case 4:
        print("Salir")
    case _:
        print("Opción no válida")
