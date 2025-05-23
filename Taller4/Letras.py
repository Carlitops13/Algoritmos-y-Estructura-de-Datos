#3.	Programa que lea 3 datos de entrada A, B y C. 
# Estos corresponden a las dimensiones de los lados de un triángulo. 
# El programa debe determinar que tipo de triangulo es, 
# teniendo en cuenta los siguiente:
#•	Si se cumple Pitágoras entonces es triángulo rectángulo
#	Si sólo dos lados del triángulo son iguales entonces es isósceles.
#	Si los 3 lados son iguales entonces es equilátero.
#	Si no se cumple ninguna de las condiciones anteriores, es escaleno.

lado_a= int(input("Ingrese el lado A: "))
lado_b= int(input("Ingrese el lado B: "))
lado_c= int(input("Ingrese el lado C: "))
if (pow(lado_a,2) + pow(lado_b,2) == pow(lado_c,2)) or (pow(lado_b,2) + pow(lado_c,2) == pow(lado_a,2)) or (pow(lado_a,2) + pow(lado_c,2) == pow(lado_b,2)):
    print("El triángulo es rectángulo")
elif lado_a==lado_b and lado_a==lado_c:
    print("El triángulo es equilátero")
elif lado_a==lado_b or lado_a==lado_c or lado_b==lado_c:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")
