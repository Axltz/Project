# Usuarios
from validaciones import confirmar_accion

class Usuario:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def validar_credenciales_admin(self, user, password):
        if user == self.user and password == self.password:
            print("Acceso permitido: admin")
            return True
        else:
            print("Credenciales incorrectas")
            return False

    def validar_credenciales_normie(self, user, password):
        if user == self.user and password == self.password:
            print("Acceso permitido: no-admin")
            return True
        else:
            print("Credenciales incorrectas")
            return False

Usuarios_normies = []
admin_user = Usuario("admin", "1234")   
usuario_active = None

def agregar_usuario():
    print("Has seleccionado registrar usuario (se necesita la autorización del ADMIN)")
    usuario = input("Usuario: ")
    contraseña = input("Password: ")

    if admin_user.validar_credenciales_admin(usuario, contraseña):  
        usuario_nuevo = input("Ingresa un nombre de usuario: ")
        contraseña_nueva = input("Ingresa una contraseña: ")
        user = Usuario(usuario_nuevo, contraseña_nueva)
        Usuarios_normies.append(user)
        print(f"Usuario '{usuario_nuevo}' agregado exitosamente.")
    else:
        print("Acceso denegado. Credenciales de admin incorrectas.")

def login_admin():
        while True:
            print("Por favor, ingresa las credenciales de admin")
            usuario = input("usuario: ")
            contraseña = input("contraseña: ")
            if admin_user.validar_credenciales_admin(usuario, contraseña):
                return True
            else:
                print("Acceso denegado. Credenciales incorrectas.")
                if not confirmar_accion("¿Deseas intentar otra vez? (si/no): "):
                    return False