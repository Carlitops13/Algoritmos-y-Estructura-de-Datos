#Prueba de Catagña Lubswer
#primera parte login
#utilizare un while
usuario = str("lubswer")
contraseña = str("catagna")
contador = 0
repeticiones = 3
#login con 3 repeticiones 
print(" Inicia sesion en el sistema ESFOT!! ")
while contador <= 3:
    usuario = input(str("Ingrese su usuario por favor: ")).lower()
    contrasena = input(str("Ingrese su por favor: ")).lower()
        
    if usuario == "lubswer".lower() and contrasena == "catagna".lower():
        print("Bienvenido al sistema!!")
        break      
    else:
         contador += 1
         print("Lo sentimos sus credenciales son incorrectas")
         print("Sus credenciales son incorrectas, lo sentimos")
#Menus y cantidad
print(" Saludos cordiales, Bienvenido al menu")
opcion1 = print("1. Poliflor + Polipeluche = $8.50")
opcion2 = print("2. Poliflor + Policarta = $3.50")
opcion3 = print("3. Poliflor + Polillavero = $4.25")
opcion4 = print("4. Poliflor + Polivaso = $2.75")
menu = float(input(" Escriba el numero de la opcion que deseee(1 al 4): "))
match menu:
    case 1:
        print("Has selecionado la opcion Poliflor + Polipeluche = $8.50")
        opcion1 = 8.5
        numeroArticulos = float(input(" Ingrese el numero de articulos que desea adquirir: "))
        valorPagar = ( numeroArticulos * opcion1 )
    case 2:
        
        print("Has selecionado la opcion Poliflor + Policarta = $3.50")
        opcion2 = 3.50
        numeroArticulos = float(input(" Ingrese el numero de articulos que desea adquirir: "))
        valorPagar = ( numeroArticulos * opcion2 )
    case 3:
        
        print("Has selecionado la opcion Poliflor + Polillavero = $4.25")
        opcion3 = 4.25
        numeroArticulos = float(input(" Ingrese el numero de articulos que desea adquirir: "))
        valorPagar = ( numeroArticulos * opcion3 )
    case 4:
        
        print("Has selecionado la opcion Poliflor + Polivaso = $2.75")
        opcion4 = 2.75
        numeroArticulos = float(input(" Ingrese el numero de articulos que desea adquirir: "))
        valorPagar = ( numeroArticulos * opcion4 )
    case _:
        print(" No has seleccionado una opcion valida ")

print(f"Heyy tu valor a pagar es: {valorPagar}")
# Seleccion tipo de pago 
print(" .....TIPO DE PAGO.....")
opcion5 = print("11. Efectivo ")
opcion6 = print("22. Tarjeta ")
tipoPago = float(input(" Escriba el tipo de pago (11 o 22): "))
match tipoPago:
    case 1:
        
        print("Seleccinoaste el tipo de pago: Efectivo, recibiras un descuento del 5%")
        opcion5 = 0.05
        costoFinal = ( opcion5 * valorPagar)
    case 2:
        
        print("Seleccionaste el tipo de pago: Tarjeta, se te informa que no tendras descuento  ")  
        opcion6 = 1 
        costoFinal = ( opcion6 * valorPagar) 
    case _:
        print("Forma de pago no valida, revisa bien la forma ( 11 o 22")

print( f"El costo final de tu orden es: {costoFinal}")
print("....MUCHAS GRACIAS por usar nuestro servicio....")
print("....Estamos a su orden y que tenga un lindo dia :)....")
