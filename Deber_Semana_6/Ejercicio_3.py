#4.	Escriba un programa que pregunte una y otra vez si desea terminar el programa,
# salvo si se contesta S o s (en mayúsculas o en minúsculas).
# Si se contesta S o s, el programa termina, en caso contrario, vuelve a preguntar.
respuesta = input("¿Desea terminar el programa? (S/s/no): ")
while respuesta.lower() != "s":
 print("El programa continuará...")
 respuesta = input("¿Desea terminar el programa? (S/s/no): ")
print("Programa finalizado.")
