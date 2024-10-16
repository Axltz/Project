from data import Proveedores
from validaciones import *
from user import *
import os

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
         #Historial_Pedidos()
         os.system('cls' if os.name == 'nt' else 'clear')
      elif seleccion == "6":
         os.system('cls' if os.name == 'nt' else 'clear')
         #Control_Ordenes()
         os.system('cls' if os.name == 'nt' else 'clear')
      elif seleccion == "0":  
         if confirmar_salida("¿Estás seguro de que deseas salir del gestor? (si/no): "):
            print("Saliendo de la opción...")
            os.system('cls' if os.name == 'nt' else 'clear')
            break
         os.system('cls' if os.name == 'nt' else 'clear')
def Mostrar_Proveedores():
    if not Proveedores:
      print("No hay proveedores registrados!")
    else:
      print("Listado de proveedores")
      for i, proveedor in enumerate(Proveedores, start=1):
        print(f"{i}. Nombre del proveedor: {proveedor['nombre']} - telefono: {proveedor['contacto']} - producto que ofrece: {proveedor['producto']}.") 
def Agregar_Proveedor():
   while True:
    if not login_admin():
          print("La autorización falló. No se puede continuar sin autorización.")
          break
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
    Mostrar_Proveedores()
          
    if not confirmar_accion("¿Deseas agregar algun otro proveedor? (si/no): "):
        os.system("cls")
        break
   os.system('cls' if os.name == 'nt' else 'clear')
def Editar_Proveedor():
   while True:
      if not login_admin():
          print("La autorización falló. No se puede continuar sin autorización.")
          break
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
      if not confirmar_accion("¿Deseas editar algún otro proveedor? (si/no)"):
          break
      os.system('cls' if os.name == 'nt' else 'clear')
def Eliminar_Proveedor():
  while True:
    if not login_admin():
          print("La autorización falló. No se puede continuar sin autorización.")
          break
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
