#4.	La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, 
# la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. 
# Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, 
# se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, 
# considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1;
# y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. 
# Realice un algoritmo para determinar la ganancia obtenida.

print ("Bienvenido a la asociación de vinicultores")

precio_inicial= 6.00
opcion= int(input("Ingrese el tipo de uva (1 o 2): "))
match opcion :
    case 1:
        print ("Uva tipo A")
        
    case 2:
        print ("Uva tipo B")
    case _:
        print ("Opción no válida")
print ("Por favor ingrese el tamaño de la uva")
tamano= int(input("Ingrese el tamaño de la uva (1 o 2): "))
match tamano:
    case 1:
        print ("Tamaño 1")
    
    case 2:
        print ("Tamaño 2")
    case _:
        print ("Opción no válida")
if opcion==1 and tamano==1:
    precio_final= precio_inicial + 0.20
    print ("El precio final de la uva es: ", precio_final)
elif opcion==1 and tamano==2:
    precio_final= precio_inicial +0.30
    print ("El precio final de la uva es: ", precio_final)
elif opcion==2 and tamano==1:
    precio_final= precio_inicial -0.30
    print ("El precio final de la uva es: ", precio_final)
elif opcion==2 and tamano==2:
    precio_final= precio_inicial -0.50
    print ("El precio final de la uva es: ", precio_final)
