#Sistema de Inventario para tienda
import os

Lista_Productos = []


def Mostrar_Productos():
    print("Listado de productos")
    for i, producto in enumerate(Lista_Productos, start=1):
        nombre = producto["nombre"]
        precio = producto["precio"]
        stock = producto["stock"]
        print(f"{i}. {nombre} - Precio por unidad: ${precio:.2f}, Cantidad: {stock} unidades")  
def Agregar_Producto():
      while True:
        print("Has seleccionado agregar un proyecto.\n")
        producto = input("Ingresa el nombre del producto: ")
        stock = int(input("Ingresa la cantidad a agregar: "))    
        precio = float(input("Ingresa el precio por unidad: "))
        nuevo_producto = {
        "nombre": producto,
        "stock": stock,
        "precio": precio
        } 
        Lista_Productos.append(nuevo_producto)
        print("Actualizando inventario...\n")
        print(f"Producto '{nuevo_producto['nombre']}' fue agregado exitosamente con {nuevo_producto['stock']} unidades en stock a un precio de ${nuevo_producto['precio']} por unidad.")

        while True:
         print("Esta es la lista actualizada: ")
         Mostrar_Productos()
         seleccion = input("¿Deseas agregar algún otro producto? si/no\n")
         if seleccion == "no":
            break
         elif seleccion == "si":
            break
         else:
            print("Opcion no valida, intente de nuevo")
        if seleccion == "no":
           print("Saliendo de la opción...")
           os.system('cls')
           break
        os.system('cls')
def Editar_Producto():
   print()
def Eliminar_Producto():
   print()


print("Has ingresado al gestor del inventario\n")
while True: 
    print("Por favor seleccione una opción:")
    print("\n\t1. Agregar producto.\n\t2. Editar producto existente.\n\t3. Eliminar producto.\n\t0. Salir\n")
    seleccion = int(input())
    if seleccion == 1:
       Agregar_Producto()
    elif seleccion == 2:
       Editar_Producto()
    elif seleccion == 3:
       Eliminar_Producto()
    elif seleccion == 0:
       break
    else: print("Opcion no valida, ingresa una existente.")