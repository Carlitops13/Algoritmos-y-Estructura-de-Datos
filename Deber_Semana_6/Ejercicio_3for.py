#Ejercicio for

#factorial de un numero
print("###FACTORIAL DE UN NÚMERO###")
numero = int(input("Ingrese un número para calcular su factorial: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print(f"El factorial de {numero} es: {factorial}")