#5.	Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) 
# y la vuelva a solicitar hasta que las dos contraseñas coincidan.

contraseña = input("Ingrese la contraseña: ")
confirmar_contraseña = input("Confirme la contraseña: ")

while contraseña != confirmar_contraseña:
    print("Las contraseñas no coinciden. Intente nuevamente.")
    contraseña = input("Ingrese la contraseña: ")
    confirmar_contraseña = input("Confirme la contraseña: ")

print("Contraseña confirmada.")