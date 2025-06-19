productos = []
id_actual = 1  # ID único para los productos

def crear_producto():
    global id_actual
    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    
    if precio.replace('.', '', 1).isdigit():
        precio = float(precio)
        producto = {"id": id_actual, "nombre": nombre, "precio": precio}
        productos.append(producto)
        print(f"Producto con ID {id_actual} creado exitosamente.\n")
        id_actual += 1
    else:
        print("Precio inválido. Debe ser un número.\n")

def ver_productos():
    if len(productos) == 0:
        print("No hay productos registrados.\n")
    else:
        print("Lista de productos:")
        for p in productos:
            print(f"ID: {p['id']} | Nombre: {p['nombre']} | Precio: ${p['precio']:.2f}")
        print()

def actualizar_producto():
    id_input = input("Ingrese el ID del producto a actualizar: ")
    if id_input.isdigit():
        id_buscar = int(id_input)
        for p in productos:
            if p["id"] == id_buscar:
                nuevo_nombre = input(f"Nuevo nombre (anterior: {p['nombre']}): ")
                nuevo_precio = input(f"Nuevo precio (anterior: {p['precio']}): ")
                if nuevo_precio.replace('.', '', 1).isdigit():
                    p["nombre"] = nuevo_nombre
                    p["precio"] = float(nuevo_precio)
                    print("Producto actualizado correctamente.\n")
                else:
                    print("Precio inválido.\n")
                return
        print("Producto no encontrado.\n")
    else:
        print("ID inválido.\n")

def eliminar_producto():
    id_input = input("Ingrese el ID del producto a eliminar: ")
    if id_input.isdigit():
        id_buscar = int(id_input)
        for p in productos:
            if p["id"] == id_buscar:
                productos.remove(p)
                print("Producto eliminado exitosamente.\n")
                return
        print("Producto no encontrado.\n")
    else:
        print("ID inválido.\n")

def mostrar_menu():
    print("----- SISTEMA DE GESTIÓN DE PRODUCTOS -----")
    print("1. Crear producto")
    print("2. Ver productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ")
    
    if opcion == "1":
        crear_producto()
    elif opcion == "2":
        ver_productos()
    elif opcion == "3":
        actualizar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.\n")






