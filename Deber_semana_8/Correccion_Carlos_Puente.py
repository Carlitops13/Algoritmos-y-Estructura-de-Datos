
clubes = []
login = "adminfifa"
password = "fifa123"

while True:
    login_usuario = input("Ingrese su usuario: ").strip().lower()
    password_usuario = input("Ingrese su contraseña: ").strip()
    
    if login_usuario == login.lower() and password_usuario == password:
        print("Bienvenido al sistema de clubes.")
        break
    else:
        print("Usuario o contraseña incorrectos. Intente nuevamente.")



while True:
    print("\nIngrese la opción que desea hacer:")
    print("1. Ingresar un nuevo club")
    print("2. Mostrar todos los clubes")
    print("3. Buscar un club") 
    print("4. Eliminar un club")
    print("5. Actualizar un club")
    print("6. Salir")

    opcion = int(input())
    if opcion == 1:
        
        while True:
            nombre = input("Ingrese el nombre del club: ").strip()
            if nombre == "":
                print("No se permiten nombres vacíos. Intente nuevamente.")
            elif nombre in clubes:
                print("El club ya está registrado.")
                break
            else:
                clubes.append(nombre)
                print("El club se ha ingresado correctamente.")
                break

    elif opcion == 2:
        
        if clubes:
            print("Los clubes registrados son:")
            for i in range(len(clubes)):
                print(f"{i+1}: {clubes[i]}")
        else:
            print("No hay clubes registrados.")

    elif opcion == 3:
        
        nombre = input("Ingrese el nombre del club que desea buscar: ").strip()
        if nombre == "":
            print("No se puede buscar un nombre vacío.")
        elif nombre in clubes:
            print("El club se encuentra en la lista.")
        else:
            print("El club no se encuentra en la lista.")

    elif opcion == 4:
        
        nombre = input("Ingrese el nombre del club que desea eliminar: ").strip()
        if nombre == "":
            print("No se puede eliminar un nombre vacío.")
        elif nombre in clubes:
            clubes.remove(nombre)
            print("El club se ha eliminado correctamente.")
        else:
            print("El club no se encuentra en la lista.")

    elif opcion == 5:
        
        nombre = input("Ingrese el nombre del club que desea actualizar: ").strip()
        if nombre == "":
            print("No se puede actualizar un nombre vacío.")
        elif nombre in clubes:
            while True:
                nuevo_nombre = input("Ingrese el nuevo nombre del club: ").strip()
                if nuevo_nombre == "":
                    print("El nuevo nombre no puede estar vacío. Intente de nuevo.")
                else:
                    clubes[clubes.index(nombre)] = nuevo_nombre
                    print("El club se ha actualizado correctamente.")
                    break
        else:
            print("El club no se encuentra en la lista.")

    elif opcion == 6:
        print("Programa finalizado.")
        break

    else:
        print("Opción incorrecta. Intente con un número del 1 al 6.")
