#Sistema de Inventario para tienda 
from user import *
from inventario import Menu_Gestor_Inventario
from visor_inventario import Menu_Inventario
from proveedores import Menu_proveedores
from ventas import Menu_ventas
from validaciones import confirmar_salida


def Menu_login():
    global usuarioIn, contraseñaIn
    intentos = 1
    max_intentos = 5
    while True:
      print("Acceso al inventario de la tienda")
      seleccion = input("\t1. Iniciar sesión\n\t2. Registrar usuario nuevo\n")
      if seleccion == "1":
        while intentos <= max_intentos:     
            print("Por favor ingresa el nombre de usuario y la contraseña")
            usuarioIn = input("Usuario: ")
            contraseñaIn = input("Contraseña: ")

            if admin_user.validar_credenciales_admin(usuarioIn, contraseñaIn):
                print("Bienvenido, Admin")
                Mostrar_Main_Menu()
                break

            usuario_encontrado = False
            for normie in Usuarios_normies:
                if normie.validar_credenciales_normie(usuarioIn, contraseñaIn):
                    print("Bienvenido, Usuario Normal")
                    usuario_encontrado = True
                    Mostrar_Main_Menu()
                    break

            if usuario_encontrado:
                break
            else:
                print("Acceso incorrecto, usuario o contraseña incorrectos")
                print(f"Te quedan {max_intentos - intentos} intentos")
                intentos += 1
        break
      elif seleccion == "2":
          agregar_usuario()


    if intentos > max_intentos:
        print("Intentos agotados, saliendo del programa...")               
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
         Menu_Gestor_Inventario()
         break
      if seleccion == "2":
         Menu_Inventario()    
         break
      if seleccion == "3":
         Menu_proveedores()
         break
      if seleccion == "4":
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

if __name__ == "__main__":
    Menu_login()


#funciones restantes a futuro:
#aplicar_descuento():
#Ordenar_productos():
#Historial_Pedidos():
#Control_Ordenes():
