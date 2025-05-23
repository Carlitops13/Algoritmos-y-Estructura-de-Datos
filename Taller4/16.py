# Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, 
# otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. 
# Si el día ingresado no es ninguno de esos, imprimir otro mensaje.

opcion = input("Ingrese un día de la semana: ").lower()
match opcion:
    case "lunes":
        print("Hoy es lunes.")
    case "viernes":
        print("Hoy es viernes.")
    case "sábado" | "domingo":
        print("Hoy es fin de semana.")
    case _:
        print("Hoy es un día de semana.")
