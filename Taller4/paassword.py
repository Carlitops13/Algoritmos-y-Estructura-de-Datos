#9.	Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada 
#en la variable sin tener en cuenta mayúsculas y minúsculas.

password= "contraseña"
password_usuario= input("Ingrese la contraseña: ")
if password_usuario.lower() == password.lower():
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")