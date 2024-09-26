import os
from validaciones import *
from data import Lista_Productos
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
