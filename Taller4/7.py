
#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. 
# Si introducimos otro número nos da un error. (Use Match)

dia = int(input("Ingrese el día de la semana (1-7): "))

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Error: Día inválido")
