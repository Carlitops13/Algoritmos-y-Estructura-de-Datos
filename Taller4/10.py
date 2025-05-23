#10.	Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
numerador = float(input("Ingrese el numerador: "))
denominador = float(input("Ingrese el denominador: "))

if denominador == 0:
    print("Error: División por cero no permitida.")
else:
    resultado = numerador / denominador
    print("El resultado de la división es:", resultado)
