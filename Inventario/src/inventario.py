import os
from validaciones import *
from visor_inventario import Mostrar_Productos
from data import Lista_Productos

def Menu_Gestor_Inventario(): 
  while True: 
      print("Has ingresado al gestor del inventario\n")
      print("Por favor seleccione una opción:")
      print("\n\t1. Agregar producto.\n\t2. Editar producto existente.\n\t3. Eliminar producto.\n\t0. Salir\n")
      seleccion = input("Elección: ")
      if seleccion == "1":
         os.system('cls' if os.name == 'nt' else 'clear')
         Agregar_Producto()
         os.system('cls' if os.name == 'nt' else 'clear')
      elif seleccion == "2":
         os.system('cls' if os.name == 'nt' else 'clear')
         Editar_Producto()
         os.system('cls' if os.name == 'nt' else 'clear')
      elif seleccion == "3":
         os.system('cls' if os.name == 'nt' else 'clear')
         Eliminar_Producto()
         os.system('cls' if os.name == 'nt' else 'clear')
      elif seleccion == "0":  
         if confirmar_salida("¿Estás seguro de que deseas salir del gestor? (si/no): "):
            print("Saliendo de la opción...")
            os.system('cls' if os.name == 'nt' else 'clear')
            break
         os.system('cls' if os.name == 'nt' else 'clear')
def Agregar_Producto():    
        while True:
          print("Has seleccionado agregar un producto.\n")
          Mostrar_Productos()
          producto = input("Ingresa el nombre del producto: ")  
          precio = validar_precio()
          stock = validar_stock()                      
          
          dic_producto = {
          "nombre": producto,
          "stock": stock,
          "precio": precio} 
            
          Lista_Productos.append(dic_producto)
          print("Actualizando inventario...\n")
          print(f"Producto '{dic_producto['nombre']}' fue agregado exitosamente con {dic_producto['stock']} unidades en stock a un precio de ${dic_producto['precio']} por unidad.")

        
          print("Esta es la lista actualizada: ")
          Mostrar_Productos()
          
          if not confirmar_accion("¿Deseas agregar algun otro producto? (si/no): "):
              os.system("cls")
              break
          os.system('cls' if os.name == 'nt' else 'clear')
def Editar_Producto():
    while True:
        print("Has seleccionado editar el inventario. ")     
        print("¿Qué producto deseas editar?")
        if not Lista_Productos:
           print("Error, no hay productos en el inventario, saliendo de la opción...")
           break
        Mostrar_Productos()
        
        seleccion = validar_seleccion("¿Qué producto deseas editar? ", Lista_Productos)
        producto = Lista_Productos[seleccion]  
        
        print("¿Qué deseas hacer? \n")
        print("\t1. Actualizar nombre.\n\t2. Actualizar stock.\n\t3. Actualizar precio.")
        seleccion = int(input("seleccion: "))
        
        if seleccion == 1: 
            producto['nombre'] = input("Ingresa el nuevo nombre del producto: ")
            print("Nombre actualizado exitosamente!")
        elif seleccion == 2:
            producto['stock'] = int(input("Ingresa el stock disponible: ")) 
            print("Stock actualizado exitosamente!")
        elif seleccion == 3:
            producto['precio'] = float(input("Ingresa el precio nuevo: ")) 
            print("Precio actualizado exitosamente!")
        else:
            print("Opción no válida.")
            continue

        print("Actualizando inventario...\n")
        print(f"Producto '{producto['nombre']}' fue editado exitosamente con {producto['stock']} unidades en stock a un precio de ${producto['precio']} por unidad.")     
        print("Esta es la lista actualizada: ")
        Mostrar_Productos()
        if not confirmar_accion("¿Deseas editar algún otro producto? "):
           break
        os.system('cls' if os.name == 'nt' else 'clear')
def Eliminar_Producto():
  while True:
    print("Has seleccionado eliminar producto")
    Mostrar_Productos()
    seleccion = validar_seleccion("¿Qué producto deseas eliminar? ", Lista_Productos)

    if confirmar_accion(f"¿Estas seguro de eliminar el producto '{Lista_Productos[seleccion]['nombre']}'? (si/no): "):
      del Lista_Productos[seleccion]
      print("Eliminando producto...")
      print("Aplicando cambios..")
      print("Producto eliminado correctamente!")
      print("Lista actualizada:\n")
      if not confirmar_accion("¿Deseas eliminar algún otro producto? (si/no)"):
        break
    else: 
      print("Has seleccionado no eliminar el producto.") 
      if not confirmar_accion("¿Deseas eliminar algún otro producto? (si/no)"):
        print("Saliendo...")
        break
      Mostrar_Productos()     
    os.system('cls' if os.name == 'nt' else 'clear')
