#Sistema de Inventario para tienda
import os
from inventario import Menu_Gestor_Inventario
from visor_inventario import Menu_Inventario
from proveedores import Menu_proveedores
from ventas import Menu_ventas
from validaciones import confirmar_salida

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
if __name__ == "__main__":
   Mostrar_Main_Menu()


#funciones restantes a futuro:
#aplicar_descuento():
#Ordenar_productos():
#Historial_Pedidos():
#Control_Ordenes():
