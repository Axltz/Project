#Sistema de Inventario para tienda
import os

Lista_Productos = []
Proveedores = []
Ventas  = []
Ingresos_totales = 0
#módulo de menus
def Mostrar_Main_Menu():
  while True:
    print("***************************")
    print("*-Gestor de negocio v1.0.-*")
    print("***************************")

    print("Bienvenido, seleccione una opción por favor.")
    print("\n\t1. Gestor del inventario.\n\t2. Visor del inventario\n\t3. Gestor de proveedores\n\t4. Ventas\n\t0. Salir del programa")
    while True:
      seleccion = input("Elección: ")
      if seleccion == "1":
         os.system('cls' if os.name == 'nt' else 'clear')
         Menu_Gestor_Inventario()
         break
      if seleccion == "2":
         os.system('cls' if os.name == 'nt' else 'clear')
         Menu_Inventario()    
         break
      if seleccion == "3":
         os.system('cls' if os.name == 'nt' else 'clear')
         Menu_proveedores()
         Menu_ventas()
         break
      if seleccion == "4":
         os.system('cls' if os.name == 'nt' else 'clear')
         Menu_ventas()         
         break
         
      elif seleccion == "0":
         break
      else: 
         print("Opción no valida, selecciona una opción existente!")
    
    if seleccion == "0":
      if confirmar_salida("¿Estás seguro de que deseas salir del programa? (si/no): "):
         print("Saliendo del programa...")
         break
      else: os.system('cls' if os.name == 'nt' else 'clear')
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
def Menu_Inventario():
   while True:
      print("Has ingresado al visor del inventario\n")
      print("Por favor seleccione una opción:")
      print("\n\t1. Mostrar inventario.\n\t2. Busqueda de inventario.\n\t3. Mostrar productos con stock bajo.\n\t4. Reabastecer productos.\n\t5. Estadisticas de stock\n\t0. Salir de la opción")
      seleccion = input("Elección: ")
      if seleccion == "1":
          os.system('cls' if os.name == 'nt' else 'clear')
          while True:
            Mostrar_Productos()
            if confirmar_salida("¿Deseas salir? (si/no): "):
               print("Saliendo...")
               break
            else: os.system('cls' if os.name == 'nt' else 'clear')
          os.system('cls' if os.name == 'nt' else 'clear')
      elif seleccion == "2":
          while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            Buscar_Producto()
            if confirmar_salida("¿Deseas salir? (si/no): "):
               print("Saliendo...")
               os.system('cls' if os.name == 'nt' else 'clear')
               break
            else: os.system('cls' if os.name == 'nt' else 'clear')
            os.system('cls' if os.name == 'nt' else 'clear')
      elif seleccion == "3":
          os.system('cls' if os.name == 'nt' else 'clear')
          while True:
            Low_Stock(umbral = 5)
            if confirmar_salida("¿Deseas salir? (si/no): "):
               print("Saliendo...")
               break
            else: os.system("cls")
            os.system('cls' if os.name == 'nt' else 'clear')
      elif seleccion == "4":
          os.system('cls' if os.name == 'nt' else 'clear')
          while True:
            Reabastecer_Producto()
            if confirmar_salida("¿Deseas salir? (si/no): "):
               print("Saliendo...")
               break
            else: os.system('cls' if os.name == 'nt' else 'clear')
            os.system('cls' if os.name == 'nt' else 'clear')
      elif seleccion == "5":
          os.system('cls' if os.name == 'nt' else 'clear')
          while True:
            Estadisticas_Stock()
            if confirmar_salida("¿Deseas salir? (si/no): "):
               print("Saliendo...")
               break
            else: os.system('cls' if os.name == 'nt' else 'clear')
            os.system('cls' if os.name == 'nt' else 'clear')
      elif seleccion == "0":
          if confirmar_salida("¿Deseas salir del visor del inventario? (si/no): "):
             print("Saliendo...")
             break
          else: os.system('cls' if os.name == 'nt' else 'clear')
          os.system('cls' if os.name == 'nt' else 'clear')
def Menu_ventas():
   while True: 
      print("Has ingresado al menú de ventas y stock.\n")
      print("Por favor seleccione una opción:")
      print("\n\t1. Realizar venta.\n\t2. Descuentos\n\t3. Reporte de ventas\n\t0. Salir\n")
      seleccion = input("Elección: ")
      if seleccion == "1":
         os.system('cls' if os.name == 'nt' else 'clear')
         Venta()
         os.system('cls' if os.name == 'nt' else 'clear')
      if seleccion == "3":
         os.system('cls' if os.name == 'nt' else 'clear')
         Reporte_Ventas()
         os.system('cls' if os.name == 'nt' else 'clear')
      if seleccion == "0":
          if confirmar_salida("¿Deseas salir del visor del inventario? (si/no): "):
             print("Saliendo...")
             break
          else: os.system('cls' if os.name == 'nt' else 'clear')
          os.system('cls' if os.name == 'nt' else 'clear')
def Menu_proveedores():
   while True:
      print("Has ingresado al gestor de proveedores.\n")
      print("Por favor seleccione una opción:")
      print("\n\t1. Mostrar Proveedores\n\t2. Agregar proveedor.\n\t3. Editar proveedor.\n\t4. Eliminar proveedor.\n\t5. Historial de pedidos.\n\t6. Ordenes\n\t0. Salir\n")
      seleccion = input("Elección: ")
      if seleccion == "1":
         os.system('cls' if os.name == 'nt' else 'clear')
         while True:
            Mostrar_Proveedores()
            if confirmar_salida("¿Deseas salir? (si/no): "):
               print("Saliendo...")
               break
            else: os.system('cls' if os.name == 'nt' else 'clear')
         os.system('cls' if os.name == 'nt' else 'clear')
      elif seleccion == "2":
         os.system('cls' if os.name == 'nt' else 'clear')
         Agregar_Proveedor()
         os.system('cls' if os.name == 'nt' else 'clear')
      elif seleccion == "3":
         os.system('cls' if os.name == 'nt' else 'clear')
         Editar_Proveedor()
         os.system('cls' if os.name == 'nt' else 'clear')
      elif seleccion == "4":
         os.system('cls' if os.name == 'nt' else 'clear')
         Eliminar_Proveedor()
         os.system('cls' if os.name == 'nt' else 'clear')
      elif seleccion == "5":
         os.system('cls' if os.name == 'nt' else 'clear')
         Historial_Pedidos()
         os.system('cls' if os.name == 'nt' else 'clear')
      elif seleccion == "6":
         os.system('cls' if os.name == 'nt' else 'clear')
         Control_Ordenes()
         os.system('cls' if os.name == 'nt' else 'clear')
      elif seleccion == "0":  
         if confirmar_salida("¿Estás seguro de que deseas salir del gestor? (si/no): "):
            print("Saliendo de la opción...")
            os.system('cls' if os.name == 'nt' else 'clear')
            break
         os.system('cls' if os.name == 'nt' else 'clear')

#Módulo de edición de productos         
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
      if not confirmar_accion("¿Deseas eliminar algún otro producto? "):
        break
    else: 
      print("Has seleccionado no eliminar el producto.") 
      if not confirmar_accion("¿Deseas eliminar algún otro producto? (si/no)"):
        print("Saliendo...")
        break
      Mostrar_Productos()     
    os.system('cls' if os.name == 'nt' else 'clear')

#módulo de visor del inventario
def Mostrar_Productos():
    if not Lista_Productos:
      print("No hay productos en el inventario!")
    else:
      print("Listado de productos")
      for i, producto in enumerate(Lista_Productos, start=1):
        print(f"{i}. {producto['nombre']} - Precio por unidad: ${producto['precio']:.2f}, Cantidad: {producto['stock']} unidades") 
def Buscar_Producto():
   Resultados = []
   while True:
      print("¿Qué producto deseas buscar?: ")
      busqueda = input().strip().lower()
      for producto in Lista_Productos:
         if busqueda in producto['nombre'].strip().lower():
            Resultados.append(producto)
      if Resultados:
         print("Productos encontrados: ")
         for producto in Resultados:
            print(f"{producto['nombre']} - Precio por unidad: ${producto['precio']} - Stock: {producto['stock']} unidades")
         break
      else:
         print("Producto no encontrado.")
def Low_Stock(umbral=5):
    print("Los siguientes productos tienen 5 o menos unidades en stock: ")
    bajo_stock = [producto for producto in Lista_Productos if producto['stock'] <= umbral]        
    if bajo_stock:
        print("Productos con stock bajo:")
        for producto in bajo_stock:
            print(f"Nombre: {producto['nombre']}, Stock: {producto['stock']}")
    else:
        print("No hay productos con stock bajo.")
def Reabastecer_Producto():
   while True:
     print("Has seleccionado 'reabastecer stock' de un producto")
     nombre = input("¿Qué producto deseas reabastecer? (escribe su nombre): ")
     producto = validar_producto(nombre)
     if producto:  
         stock = int(input("Ingresa la cantidad de stock a agregar: "))
         re_stock(producto, stock) 
         if not confirmar_accion("¿Deseas reabastecer otro producto? (si/no): "):
            os.system('cls' if os.name == 'nt' else 'clear')
            break
     else:
         print("Producto no encontrado.")
         if confirmar_salida("¿Deseas salir de la opción? (si/no): "):
          os.system('cls' if os.name == 'nt' else 'clear')
          break
def re_stock(producto, stock): 
    producto['stock'] += stock  
    print(f"Stock del producto actualizado, nuevo stock: {producto['stock']}")
def Estadisticas_Stock():
   while True:
     total_productos = len(Lista_Productos)
     total_stock = sum(producto['stock'] for producto in Lista_Productos)
     print(f"Total de productos: {total_productos}")
     print(f"Total de stock: {total_stock}")
     break
#módulo de proveedores
def Mostrar_Proveedores():
    if not Proveedores:
      print("No hay proveedores registrados!")
    else:
      print("Listado de proveedores")
      for i, proveedor in enumerate(Proveedores, start=1):
        print(f"{i}. Nombre del proveedor: {proveedor['nombre']} - telefono: {proveedor['contacto']} - producto que ofrece: {proveedor['producto']}.") 
def Agregar_Proveedor():
   while True:
    print("Has seleccionado agregar un proveedor.\n")
    Mostrar_Proveedores()
    nombre_proveedor = input("Ingresa el nombre del proveedor: ")  
    telefono = input("Ingresa el número de contacto del proveedor: ")
    producto = input("¿Qué producto ofrece el proveedor: ")                     
          
    dic_proveedores = {
      "nombre": nombre_proveedor,
      "contacto": telefono,
      "producto": producto} 
            
    Proveedores.append(dic_proveedores)
    print("Actualizando inventario...\n")
    print(f"proveedor '{dic_proveedores['nombre']}' fue agregado exitosamente.")

        
    print("Esta es la lista de proveedores actualizada: ")
    Mostrar_Productos()
          
    if not confirmar_accion("¿Deseas agregar algun otro proveedor? (si/no): "):
        os.system("cls")
        break
   os.system('cls' if os.name == 'nt' else 'clear')
def Editar_Proveedor():
   while True:
      print("Has seleccionado editar proveedores. ")     
      print("¿Qué producto deseas editar?")
      if not Proveedores:
          print("Error, no hay proveedores registrados, saliendo de la opción...")
          break
      Mostrar_Proveedores()
        
      seleccion = validar_seleccion("¿Qué proveedor deseas editar? ", Proveedores)
      proveedor = Proveedores[seleccion]  
        
      print("¿Qué deseas hacer? \n")
      print("\t1. Actualizar nombre.\n\t2. Actualizar telefono.\n\t3. Actualizar producto que ofrece.")
      seleccion = int(input("seleccion: "))
        
      if seleccion == 1: 
          proveedor['nombre'] = input("Ingresa el nuevo nombre del proveedor: ")
          print("Nombre actualizado exitosamente!")
      elif seleccion == 2:
          proveedor['contacto'] = int(input("Ingresa el nuevo número de telefono: ")) 
          print("Teléfono actualizado exitosamente!")
      elif seleccion == 3:
          proveedor['producto'] =input("Ingresa el producto que ofrece: ")
          print("Producto ofertado actualizado exitosamente!")
      else:
          print("Opción no válida.")
          continue

      print("Actualizando inventario...\n")
      print(f"Proveedor '{proveedor['nombre']}' fue editado exitosamente.")     
      print("Esta es la lista de proveedores actualizada: ")
      Mostrar_Proveedores()
      if not confirmar_accion("¿Deseas editar algún otro proveedor? "):
          break
      os.system('cls' if os.name == 'nt' else 'clear')
def Eliminar_Proveedor():
  while True:
    print("Has seleccionado eliminar proveedor")
    Mostrar_Proveedores()
    seleccion = validar_seleccion("¿Qué proveedor deseas eliminar? ", Proveedores)

    if confirmar_accion(f"¿Estas seguro de eliminar el proveedor '{Proveedores[seleccion]['nombre']}'? (si/no): "):
      del Proveedores[seleccion]
      print("Eliminando proveedor...")
      print("Aplicando cambios..")
      print("Proveedor eliminado correctamente!")
      print("Lista actualizada:\n")
      if not confirmar_accion("¿Deseas eliminar algún otro proveedor? "):
        break
    else: 
      print("Has seleccionado no eliminar el proveedor.") 
      if not confirmar_accion("¿Deseas eliminar algún otro proveedor? (si/no)"):
        print("Saliendo...")
        break
      Mostrar_Proveedores()     
    os.system('cls' if os.name == 'nt' else 'clear')

#módulo de ventas y estadisticas
def Venta():
    while True:
        print("Has ingresado al apartado de ventas.\n")
        print("Esta es la lista del inventario.")
        while True:
            print("¿Qué producto deseas vender? (ingresa su nombre): ")
            Mostrar_Productos()
            nombre = input()
            if not validar_producto(nombre):
                print("Producto inexistente!")
                continue  
            print("¿Cuánta cantidad se venderá?: ")
            stock = int(input())
            Hacer_venta(nombre, stock) 
            if not confirmar_accion("¿Deseas vender otro producto? (si/no): "):
                break  
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
        if confirmar_salida("¿Deseas salir de la opción? (si/no): "):
            break  
def Hacer_venta(nombre, stock):
    global Ingresos_totales 
    for producto in Lista_Productos:
        if producto['nombre'] == nombre:
            if producto['stock'] >= stock: 
                total_venta = float(producto['precio'] * stock) 
                print(f"Total a pagar: ${total_venta:.2f}")

                if confirmar_accion("¿Deseas confirmar la venta? (si/no): "):
                    producto['stock'] -= stock  
                    ventas_dicc = {
                        'Nombre_del_producto': producto['nombre'],
                        'cantidad_vendida': stock, 
                        'precio_unitario': producto['precio'],
                        'precio_total' : total_venta
                    }
                    Ventas.append(ventas_dicc) 
                    print(f"Has vendido {stock} unidades de '{producto['nombre']}'.")
                    Ingresos_totales += total_venta  
                else:
                    print("Venta cancelada.")
            else:
                print("¡Stock insuficiente para realizar la venta!")
                print("Cancelando la operación...")
def Reporte_Ventas():
   while True:
     print("Has seleccionado ver el reporte de ventas.")
     if not Ventas:
        print("No hay ventas aún!")
     else:
        print("El historial de ventas es el siguiente:\n")
        for i, producto in enumerate(Ventas, start=1):
          print(f"{i}. {producto['Nombre_del_producto']} - Precio por unidad: ${producto['precio_unitario']:.2f}, Cantidades vendidas: {producto['cantidad_vendida']} unidades, total de venta: ${producto['precio_total']:.2f}") 
     print(f"Los ingresos totales son: ${Ingresos_totales:.2f}")
     if confirmar_salida("¿Deseas salir de la opción? (si/no): "):
        break

#módulo de validaciones, confirmaciones y herramientas extras
def validar_producto(nombre):
    for producto in Lista_Productos:
        if producto['nombre'].lower() == nombre.lower():
            print("Producto encontrado exitosamente!")
            return producto
    print("Producto inexistente en el inventario!")
    return None
def validar_precio():
   while True:
           try:
             precio = float(input("Ingresa el precio por unidad: "))
             if precio > 0:
               return precio
             else:
               print("El precio debe ser mayor a 0.")  
           except ValueError:
              print("Debes ingresar un número válido.") 
def validar_stock():
   while True:
             try:
              stock = int(input("Ingresa la cantidad a agregar: "))  
              if stock > 0:
                return stock
              else:
                print("El stock debe ser mayor a 0.")  
             except ValueError:
                print("Debes ingresar un número válido.") 
def validar_seleccion(mensaje, lista):
    while True:
        try:
            seleccion = int(input(mensaje)) - 1
            if 0 <= seleccion < len(lista):
                return seleccion
            else:
                print("Opción no válida, intente de nuevo.")
        except ValueError:
            print("Debe ingresar un número válido.")
def confirmar_salida(mensaje):
    while True:
        confirmacion = input(mensaje).strip().lower()
        if confirmacion == "si":
            return True
        elif confirmacion == "no":
            return False
        else:
            print("Opción no válida, ingresa 'si' o 'no'.")
def confirmar_accion(mensaje):
    while True:
        confirmacion = input(mensaje).strip().lower()
        if confirmacion == "si":
            return True
        elif confirmacion == "no":
            return False
        else:
            print("Opción no válida, ingresa 'si' o 'no'.")

if __name__ == "__main__":
   Mostrar_Main_Menu()

#funciones restantes   


def aplicar_descuento():
   print()
def Ordenar_productos():
   print()
def Historial_Pedidos():
   print()
def Control_Ordenes():
   print()
