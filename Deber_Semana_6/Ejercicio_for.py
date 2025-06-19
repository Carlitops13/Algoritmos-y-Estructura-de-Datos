# 5 ejercicicio for
# 1 Login

usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")
for i in range(3):
    usuario_ingresado = input("Ingrese su nombre de usuario: ")
    contraseña_ingresada = input("Ingrese su contraseña: ")
    
    if usuario_ingresado == usuario and contraseña_ingresada == contraseña:
        print("¡Bienvenido!")
        break
    else:
        print("Usuario o contraseña incorrectos. Intente nuevamente.")
        
    