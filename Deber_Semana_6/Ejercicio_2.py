#2.	Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí (en minúsculas y con tilde).
#No use funciones

respuesta = input("¿Desea continuar con el programa? (sí/no): ")
while respuesta == "sí":
    print("Continuando con el programa...")
    respuesta = input("¿Desea continuar con el programa? (sí/no): ")
print("Programa finalizado.")
