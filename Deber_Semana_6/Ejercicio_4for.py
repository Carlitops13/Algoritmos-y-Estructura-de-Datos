#  vocales en una palabra 

palabra = input("Ingrese una palabra: ").lower()
vocales = "aeiou"
contador_vocales = 0
for letra in palabra:
    if letra in vocales:
        contador_vocales += 1
print(f"La palabra '{palabra}' tiene {contador_vocales} vocales.")