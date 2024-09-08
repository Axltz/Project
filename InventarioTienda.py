#Sistema de Inventario para tienda
import os

Lista_Productos = []

os.system("color 02")
def Mostrar_Productos():
    print("Listado de productos")
    for i, producto in enumerate(Lista_Productos, start=1):
        print(f"{i}. {producto['nombre']} - Precio por unidad: ${producto['precio']:.2f}, Cantidad: {producto['stock']} unidades")  
def Agregar_Producto():
      while True:
        print("Has seleccionado agregar un producto.\n")
        Mostrar_Productos()
        producto = input("Ingresa el nombre del producto: ")
        stock = int(input("Ingresa la cantidad a agregar: "))    
        precio = float(input("Ingresa el precio por unidad: "))
        dic_producto = {
        "nombre": producto,
        "stock": stock,
        "precio": precio} 
        
        Lista_Productos.append(dic_producto)
        print("Actualizando inventario...\n")
        print(f"Producto '{dic_producto['nombre']}' fue agregado exitosamente con {dic_producto['stock']} unidades en stock a un precio de ${dic_producto['precio']} por unidad.")

        while True:
         print("Esta es la lista actualizada: ")
         Mostrar_Productos()
         seleccion = input("¿Deseas agregar algún otro producto? si/no\n")
         if seleccion == "no":
            print("Saliendo de la opción...")
            break
         elif seleccion == "si":
            break
         else:
            print("Opcion no valida, intente de nuevo")
        if seleccion == "no":
           print("Saliendo de la opción...")      
           break
        os.system("cls")
def Editar_Producto():
    while True:
        print("Has seleccionado editar el inventario. ")     
        print("¿Qué producto deseas editar?")
        Mostrar_Productos()
        seleccion = int(input("Selección: ")) -1
        
        if seleccion < 0 or seleccion >= len(Lista_Productos):
            print("Selección inválida.")
            continue
        
        producto = Lista_Productos[seleccion]  
        
        print("¿Qué deseas hacer? \n")
        print("\t1. Actualizar nombre.\n\t2. Actualizar stock.\n\t3. Actualizar precio.")
        accion = int(input("Acción: "))
        
        if accion == 1: 
            producto['nombre'] = input("Ingresa el nuevo nombre del producto: ")
            print("Nombre actualizado exitosamente!")
        elif accion == 2:
            producto['stock'] = int(input("Ingresa el stock disponible: ")) 
            print("Stock actualizado exitosamente!")
        elif accion == 3:
            producto['precio'] = float(input("Ingresa el precio nuevo: ")) 
            print("Precio actualizado exitosamente!")
        else:
            print("Opción no válida.")
            continue

        print("Actualizando inventario...\n")
        print(f"Producto '{producto['nombre']}' fue editado exitosamente con {producto['stock']} unidades en stock a un precio de ${producto['precio']} por unidad.")

        while True:
            print("Esta es la lista actualizada: ")
            Mostrar_Productos()
            seleccion = input("¿Deseas editar algún otro producto? si/no\n")
            if seleccion == "no":
                break
            elif seleccion == "si":
                break
            else:
                print("Opción no válida, intente de nuevo")
        if seleccion == "no":
         break
        os.system("cls")
def Eliminar_Producto():
  while True:
    print("Has seleccionado eliminar producto")
    print("¿Qué producto deseas eliminar?")
    Mostrar_Productos()
    seleccion = int(input()) - 1
    del Lista_Productos[seleccion]
    print("Eliminando producto...")
    print("Aplicando cambios..")
    print("Producto eliminado correctamente!")
    print("Lista actualizada:\n")
    Mostrar_Productos()
    while True: 
      print("Deseas eliminar algún otro? si/no")
      seleccion = input()
      if seleccion == "si":
         break
      elif seleccion == "no":
         break
      else:
         print("Opción no valida, intenta otra vez.")
         os.system("cls")
    if seleccion == "no":
       break

while True: 
    print("Has ingresado al gestor del inventario\n")
    print("Por favor seleccione una opción:")
    print("\n\t1. Agregar producto.\n\t2. Editar producto existente.\n\t3. Eliminar producto.\n\t0. Salir\n")
    seleccion = int(input())
    if seleccion == 1:
       Agregar_Producto()
       os.system('cls')
    elif seleccion == 2:
       Editar_Producto()
       os.system('cls')
    elif seleccion == 3:
       Eliminar_Producto()
       os.system('cls') 
    elif seleccion == 0:
       os.system('cls')
       break
    else: print("Opcion no valida, ingresa una existente.")