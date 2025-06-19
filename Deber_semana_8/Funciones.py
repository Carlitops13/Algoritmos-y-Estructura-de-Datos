#Ejemplo 3 de matrices

def convertirBinario(decimal):
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2
    return binario

binario=int(input("Ingrese un numero decimal: "))
print("El numero binario es: ",convertirBinario(binario))




