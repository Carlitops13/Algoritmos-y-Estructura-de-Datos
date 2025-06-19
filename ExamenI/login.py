# Login 2 pts. El  sistema  debe  tener  un  login  de  acceso 
# en  el  cual  se pedirá el ingreso del usuario y el password.   
# • Email: admin@epn.edu.ec  • Password: ClaveFuerte* En  el  caso  de  que 
# las  credenciales  no  sean  ingresadas de forma correcta no se puede ingresar al sistema y se le  solicitará  
# que  ingrese  las  credenciales  correctas. 
# (Presentar nuevamente el login de forma indefinida). 

contador = 0
while contador < 3:
    email = input("Ingrese su email: ")
    password = input("Ingrese su password: ")

    if email == "admin@epn.edu.ec" and password == "ClaveFuerte*":
        print("Login exitoso.")
        break
    else:
        print("Credenciales incorrectas. Intente nuevamente.")