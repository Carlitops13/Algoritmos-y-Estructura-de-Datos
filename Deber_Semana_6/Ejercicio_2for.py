numeros = [3, 10, 5, 8, 2, 15, 6]

limite = int(input("Mostrar solo los números mayores que: "))
mayores = []

for num in numeros:
    if num > limite:
        mayores.append(num)

print(f"Números mayores que {limite}: {mayores}")