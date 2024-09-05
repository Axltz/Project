#Sistema de Inventario para tienda
import os

Lista_Productos = []
Nombres =  []
Precios = []
Stock = []

def Mostrar_Productos():
    print("Listado de productos")
    for i, productos in enumerate(Lista_Productos, start=1):
        Nombres, Precios, Stock = productos
        print(f"{i}. {Nombres} - Precio por unidad: ${Precios:.2f}, Cantidad: {Stock} unidades")
