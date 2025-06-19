# 1.	Escriba un programa que imprima la tabla de multiplicar indicada por el usuario,
# pregunte al usuario que ingrese el número de la tabla a multiplicar, imprima toda la tabla hasta el 12:
i = 0 
numero=  int(input("Ingrese el número de la tabla a multiplicar: "))
print("###TABLA DE MULTIPLICAR###")
while i < 13:
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
    i += 1



    
