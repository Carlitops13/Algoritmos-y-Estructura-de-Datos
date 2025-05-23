#12.	Hacer el programa anterior considerando que las personas mayores  65 años para la mitad del impuesto.
edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos mensuales: "))

if edad > 16 and ingresos >= 1000:
    if edad > 65:
        print("Usted tiene que tributar, pero tiene un descuento del 50%.")
    else:
        print("Usted tiene que tributar.")
else:
    print("Usted no tiene que tributar.")
