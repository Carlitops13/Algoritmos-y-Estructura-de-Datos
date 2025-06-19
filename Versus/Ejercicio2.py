# #Ejercicio 2: Lista de Tareas
# #Objetivo: Diseñar un programa que gestione una lista de tareas simple.
#
# El programa debe ser un menú que se repita y ofrezca las siguientes opciones:
#
# Agregar tarea: Pide al usuario que escriba una nueva tarea y la añade a una lista.
# Ver tareas: Muestra todas las tareas pendientes, numeradas (ej. "1. Lavar la ropa"). Si no hay tareas, debe indicarlo.
# Marcar como completada: Muestra las tareas numeradas, le pregunta al usuario qué número de tarea desea eliminar, y la quita de la lista.
# Salir: Termina el programa.
# Conceptos Clave a Demostrar:
#
# Uso de un bucle while para que el menú se repita.
# Manejo de la lógica del menú con if/elif/else.
# Uso de listas y sus métodos como .append() y .pop().
# Iterar sobre la lista con enumerate() para mostrar las tareas numeradas.

tareas = []

while True:
    print("\nMenu Tareas:")
    print("1. Añade una tarea")
    print("2. Ver Tareas") 
    print("3. Marcar tarea completada")
    print("4. Exit")
    
    opcion = input("\nSeleciona una opcion(1,2,3 o 4) ")
    
    if opcion == "1":
        nuevaTarea = input("Ingresa una tarea nueva: ")
        tareas.append(nuevaTarea)
        print("Tarea añadida!")
        
    elif opcion == "2":
        if not tareas:
            print("No hay tareas pendientes")
        else:
            print("\nTareas Pendientes")
            for i in range(len(tareas)):
                print(f"{i + 1}. {tareas[i]}")
                
    elif opcion == "3":
        if not tareas:
            print("No hay tareas pendientes")
            
        else:
            print("\nTareas Pendientes")
        for i in range(len(tareas)):
               print(f"{i + 1}. {tareas[i]}")
               num_tarea = int(input("\nIngrese el numero de tareas marcadas como completas "))
               if 1 <= num_tarea <= len(tareas):
                tareaCompletada = tareas.pop(num_tarea- 1)
                print(f"tarea '{tareaCompletada}' marcada como completada")
               else:
                print("Numero invalido de tarea")
                
    elif opcion == "4":
        print("Adios")
        break
        
    else:
        print("Opcion  Invalida")

