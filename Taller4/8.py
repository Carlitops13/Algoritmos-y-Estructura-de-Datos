#8.	Considera que estás desarrollando un programa donde trabajas con tipos de motor 
# (suponemos que se trata del tipo de motor de una bomba para mover fluidos). 
# Crea una función denominada dimeTipoMotor() donde pidas el tipo de motor al usuario 
# (indicando que los valores posibles son 1, 2, 3, 4) y a través de un condicional switch hagas lo siguiente: 
# a) Si el tipo de motor es 0, mostrar un mensaje indicando “No hay establecido un valor definido para el tipo de bomba”. 
# b) Si el tipo de motor es 1, mostrar un mensaje indicando “La bomba es una bomba de agua”. 
# c) Si el tipo de motor es 2, mostrar un mensaje indicando “La bomba es una bomba de gasolina”. 
# d) Si el tipo de motor es 3, mostrar un mensaje indicando “La bomba es una bomba de hormigón”. 
# e) Si el tipo de motor es 4, mostrar un mensaje indicando “La bomba es una bomba de pasta alimenticia”. 
# f) Si no se cumple ninguno de los valores anteriores mostrar el mensaje “No existe un valor válido para tipo de bomba”. 
# Ejecuta el código y comprueba sus resultados

def dimeTipoMotor():
    tipo_motor = int(input("Ingrese el tipo de motor (1-4): "))
    match tipo_motor:
        case 0:
            print("No hay establecido un valor definido para el tipo de bomba")
        case 1:
            print("La bomba es una bomba de agua")
        case 2:
            print("La bomba es una bomba de gasolina")
        case 3:
            print("La bomba es una bomba de hormigón")
        case 4:
            print("La bomba es una bomba de pasta alimenticia")
        case _:
            print("No existe un valor válido para tipo de bomba")

dimeTipoMotor() 