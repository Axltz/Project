#Sistema de Inventario para tienda
import os

Lista_Productos = []
Nombres =  [1,2,3]
Precios = [1,2,3]
Stock = [1,2,3]
Lista_Productos.append(Nombres)
Lista_Productos.append(Precios)
Lista_Productos.append(Stock)
def Mostrar_Productos():
    print("Listado de productos")
    for i, productos in enumerate(Lista_Productos, start=1):
        Nombres, Precios, Stock = productos
        print(f"{i}. {Nombres} - Precio por unidad: ${Precios:.2f}, Cantidad: {Stock} unidades")
Mostrar_Productos()