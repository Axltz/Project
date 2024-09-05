#Sistema de Inventario para tienda
import os

Lista_Productos = []
Nombres =  []
Precios = []
Stock = []
Lista_Productos.append(Nombres)
Lista_Productos.append(Precios)
Lista_Productos.append(Stock)

def Ver_Productos():
    for i, producto in enumerate(Lista_Productos, start=1):
      Nombres, Stock, Precios = producto
      print(f"{i}. Nombre: {Nombres}, Cantidad: {Stock}, Precio por unidad: ${Precios:.2f}")
def Agregar_Productos():
   print("Has seleccionado agregar productos.\n")
   producto = input("Ingresa el nombre del producto: ")
   Nombres.append(producto)
   precio = input()
