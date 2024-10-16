from data import Lista_Productos, Ventas, Ingresos_totales
from validaciones import *
from visor_inventario import Mostrar_Productos
from user import *


def Menu_ventas():
   while True: 
      print("Has ingresado al menú de ventas y stock.\n")
      print("Por favor seleccione una opción:")
      print("\n\t1. Realizar venta.\n\t2. Descuentos\n\t3. Reporte de ventas\n\t0. Salir\n")
      seleccion = input("Elección: ")
      if seleccion == "1":
         Venta()
      if seleccion == "3":
         Reporte_Ventas()
      if seleccion == "0":
          if confirmar_salida("¿Deseas salir del visor del inventario? (si/no): "):
             print("Saliendo...")
             break        
def Venta():
    while True:
        print("Has ingresado al apartado de ventas.\n")
        print("Esta es la lista del inventario.")
        while True:
            print("¿Qué producto deseas vender? (ingresa su nombre): ")
            Mostrar_Productos()
            if not Lista_Productos:
                if confirmar_salida("¿Deseas salir de la opción? (si/no): "):
                    break
            nombre = input()
            if not validar_producto(nombre):
                print("Producto inexistente!") 
                continue  
            print("¿Cuánta cantidad se venderá?: ")
            stock = int(input())
            Hacer_venta(nombre, stock) 
            if not confirmar_accion("¿Deseas vender otro producto? (si/no): "):
                break  
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
     if not login_admin():
          print("La autorización falló. No se puede continuar sin autorización.")
          break
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
