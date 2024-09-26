from data import Lista_Productos

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
