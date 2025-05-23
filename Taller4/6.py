#6.	Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, 
# América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte se basa
# en el peso del paquete y la zona a la que va dirigido. 
# Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, 
# esto por cuestiones de logística y de seguridad. Realice un algoritmo para determinar el cobro 
# por la entrega de un paquete o, en su caso, el rechazo de la entrega.

americaNorte= 24.00
americaCentral=20.00
americaSur=21.00
europa= 10.00
asia= 18.00
peso= float(input("Ingrese el peso del paquete:"))

print("1. América del Norte")
print("2. América Central")
print("3. América del Sur")
print("4. Europa")
print("5. Asia")
zona= int(input("Ingrese la zona a la que va dirigido el  paquete: "))
match zona:
    case 1:
        costo = americaNorte * peso
    case 2:
        costo = americaCentral * peso
    case 3:
        costo = americaSur * peso
    case 4:
        costo = europa * peso
    case 5:
        costo = asia * peso
    case _:
        print("La zona no es válida") 
if peso > 5:
    print("El paquete no es transportado")
elif peso <= 5 and costo != 0:
    print("El costo del paquete es: ", costo)
    